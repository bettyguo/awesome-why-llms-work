"""Verify every arXiv link in the repository resolves and that the cited year
and first author surname plausibly match the entry text.

Usage:
    python scripts/verify_citations.py [--strict] [--paths path1 path2 ...]

Default behavior (no --paths): scans README.md, programmes/, essays/, GLOSSARY.md,
reading-paths/, and adjacent-programmes appendices.

Exit codes:
    0  all verified
    1  one or more citations could not be verified
    2  network or unexpected error

This script is designed to run in CI. It is conservative about what it flags:
- arXiv IDs that 404 are hard failures.
- Year-mismatch flags are warnings unless --strict is passed.
- Author-mismatch flags are warnings unless --strict is passed.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ARXIV_API = "http://export.arxiv.org/api/query?id_list={ids}"
ARXIV_LINK_RE = re.compile(r"https?://arxiv\.org/abs/(?P<id>[0-9]{4}\.[0-9]{4,5})")

DEFAULT_SCAN_ROOTS = [
    "README.md",
    "GLOSSARY.md",
    "DECISIONS.md",
    "CONTRIBUTING.md",
    "programmes",
    "essays",
    "reading-paths",
    "tracker",
]


@dataclass
class Citation:
    arxiv_id: str
    file: Path
    line_no: int
    line: str


def find_citations(paths: Iterable[Path]) -> list[Citation]:
    out: list[Citation] = []
    for p in paths:
        if p.is_dir():
            for f in p.rglob("*.md"):
                out.extend(find_citations([f]))
            continue
        if not p.exists() or not p.is_file():
            continue
        if p.suffix != ".md":
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
            for m in ARXIV_LINK_RE.finditer(line):
                out.append(Citation(arxiv_id=m.group("id"), file=p, line_no=i, line=line))
    return out


def fetch_arxiv(ids: list[str]) -> dict[str, dict]:
    """Returns a dict id -> {title, authors, year} for valid IDs. Missing IDs
    are simply absent from the result. Batches 10 at a time with retry."""
    by_id: dict[str, dict] = {}
    if not ids:
        return by_id
    BATCH = 5
    headers = {"User-Agent": "awesome-why-llms-work/1.0 (citation-verify; +https://arxiv.org/help/api)"}
    print(f"  querying arXiv API for {len(ids)} unique IDs in batches of {BATCH} ...", file=sys.stderr)
    for i in range(0, len(ids), BATCH):
        batch = ids[i : i + BATCH]
        url = ARXIV_API.format(ids=",".join(batch))
        xml = None
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=60) as resp:
                    xml = resp.read().decode("utf-8")
                break
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                print(f"  network error (attempt {attempt+1}/4) on batch {i//BATCH + 1}: {e}", file=sys.stderr)
                time.sleep(5.0 * (attempt + 1))
        if xml is None:
            print(f"  giving up on batch {batch}", file=sys.stderr)
            continue
        ns = {"a": "http://www.w3.org/2005/Atom"}
        try:
            root = ET.fromstring(xml)
        except ET.ParseError as e:
            print(f"  XML parse error: {e}", file=sys.stderr)
            continue
        for entry in root.findall("a:entry", ns):
            id_el = entry.find("a:id", ns)
            title_el = entry.find("a:title", ns)
            pub_el = entry.find("a:published", ns)
            authors = [
                (a.find("a:name", ns).text or "") for a in entry.findall("a:author", ns)
            ]
            if id_el is None or id_el.text is None:
                continue
            m = re.search(r"abs/([0-9]{4}\.[0-9]{4,5})", id_el.text)
            if not m:
                continue
            aid = m.group(1)
            by_id[aid] = {
                "title": (title_el.text or "").strip() if title_el is not None else "",
                "authors": authors,
                "year": (pub_el.text or "")[:4] if pub_el is not None else "",
            }
        time.sleep(3.0)  # be polite to the arXiv API
    return by_id


YEAR_RE = re.compile(r"\b(20\d{2})\b")


def author_surnames(authors: list[str]) -> list[str]:
    out = []
    for a in authors:
        parts = a.strip().split()
        if parts:
            out.append(parts[-1].lower())
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat year and author mismatches as hard failures.",
    )
    parser.add_argument(
        "--paths",
        nargs="*",
        default=None,
        help="Optional file or directory paths to scan. Default: repo defaults.",
    )
    args = parser.parse_args()

    if args.paths:
        scan = [Path(p) for p in args.paths]
    else:
        scan = [Path(p) for p in DEFAULT_SCAN_ROOTS]

    citations = find_citations(scan)
    if not citations:
        print("no citations found")
        return 0

    unique_ids = sorted({c.arxiv_id for c in citations})
    print(f"found {len(citations)} citations referencing {len(unique_ids)} unique arXiv IDs")
    metadata = fetch_arxiv(unique_ids)

    hard_failures = 0
    soft_failures = 0
    for c in citations:
        meta = metadata.get(c.arxiv_id)
        if meta is None:
            print(f"FAIL  {c.file}:{c.line_no}  arXiv:{c.arxiv_id} not found")
            hard_failures += 1
            continue
        warnings: list[str] = []
        # Year check: look for any 4-digit year in the line, see if metadata year matches one of them.
        years_in_line = set(YEAR_RE.findall(c.line))
        if years_in_line and meta["year"] and meta["year"] not in years_in_line:
            # Allow off-by-one (revisions, ICLR proceedings, etc.)
            close = any(abs(int(meta["year"]) - int(y)) <= 1 for y in years_in_line)
            if not close:
                warnings.append(f"year mismatch (api={meta['year']}, line={sorted(years_in_line)})")
        # Author check: first author surname should appear in the line (case-insensitive).
        if meta["authors"]:
            first_surname = author_surnames(meta["authors"])[0]
            if first_surname and first_surname not in c.line.lower():
                # Try last surname too (some entries list last author)
                surnames_lower = author_surnames(meta["authors"])
                if not any(s in c.line.lower() for s in surnames_lower):
                    warnings.append(f"first-author surname '{first_surname}' not found in line")
        if warnings:
            tag = "FAIL" if args.strict else "WARN"
            for w in warnings:
                print(f"{tag}  {c.file}:{c.line_no}  arXiv:{c.arxiv_id}  {w}")
            if args.strict:
                hard_failures += len(warnings)
            else:
                soft_failures += len(warnings)
        else:
            pass  # silent on success
    n_ok = len(citations) - hard_failures - soft_failures
    print(f"\nsummary: {n_ok}/{len(citations)} verified; {soft_failures} warnings; {hard_failures} hard failures")
    return 1 if hard_failures else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:  # noqa: BLE001
        print(f"unexpected error: {e}", file=sys.stderr)
        sys.exit(2)
