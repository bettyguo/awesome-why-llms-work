"""Check that every external URL in the repo's Markdown files resolves with a
200-class HTTP response.

Usage:
    python scripts/check_links.py [--timeout 15] [--max-workers 8] [--exclude PATTERN]

Exits with status 1 on any failed link; 0 on success.

This script is the runtime link checker complementing scripts/verify_citations.py
(which only checks arXiv references). check_links.py covers all https://* URLs.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

URL_RE = re.compile(r"https?://[^\s)<>\"]+")

# Hosts that frequently 403 to scrapers but are still valid in practice;
# we still attempt them but treat 403 as a soft pass.
SOFT_403_HOSTS = (
    "openai.com",
    "twitter.com",
    "x.com",
    "linkedin.com",
)


def extract_urls(paths: list[Path]) -> dict[str, list[tuple[Path, int]]]:
    out: dict[str, list[tuple[Path, int]]] = {}
    for root in paths:
        if root.is_dir():
            files = list(root.rglob("*.md"))
        else:
            files = [root]
        for f in files:
            for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                for m in URL_RE.finditer(line):
                    url = m.group(0).rstrip(".,;:")
                    out.setdefault(url, []).append((f, i))
    return out


def check_one(url: str, timeout: float) -> tuple[str, int | None, str | None]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "awesome-why-llms-work/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return url, resp.status, None
    except urllib.error.HTTPError as e:
        # Try GET on 405 (Method Not Allowed) — some servers don't support HEAD.
        if e.code == 405:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "awesome-why-llms-work/1.0"})
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    return url, resp.status, None
            except urllib.error.HTTPError as e2:
                return url, e2.code, str(e2)
            except urllib.error.URLError as e2:
                return url, None, str(e2)
        return url, e.code, str(e)
    except urllib.error.URLError as e:
        return url, None, str(e)
    except Exception as e:  # noqa: BLE001
        return url, None, repr(e)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--timeout", type=float, default=20.0)
    p.add_argument("--max-workers", type=int, default=8)
    p.add_argument("--exclude", default=None, help="regex; URLs matching are skipped")
    p.add_argument("--paths", nargs="*", default=None)
    args = p.parse_args()

    if args.paths:
        paths = [Path(x) for x in args.paths]
    else:
        paths = [Path(".")]

    urls = extract_urls(paths)
    if args.exclude:
        rex = re.compile(args.exclude)
        urls = {u: refs for u, refs in urls.items() if not rex.search(u)}

    print(f"checking {len(urls)} unique URLs ...")
    failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as ex:
        futs = {ex.submit(check_one, u, args.timeout): u for u in urls}
        for fut in concurrent.futures.as_completed(futs):
            url, status, err = fut.result()
            ok = status is not None and 200 <= status < 400
            if not ok and status == 403 and any(h in url for h in SOFT_403_HOSTS):
                ok = True
                status = 403  # we still print it
            if not ok:
                failed += 1
                print(f"FAIL  {url}  status={status}  err={err}")
                for f, i in urls[url][:3]:
                    print(f"        referenced at {f}:{i}")
    if failed:
        print(f"\nsummary: {failed} failed; {len(urls) - failed} ok")
        return 1
    print("all links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
