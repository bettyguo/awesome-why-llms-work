"""Render the falsification-ledger summary table by counting status emojis in
each programme file's "Falsification Status" section.

Usage:
    python scripts/render_ledger.py [--write-readme]

Without --write-readme: prints a fresh markdown table to stdout.
With    --write-readme: replaces the table inside README.md between the
                       markers <!-- LEDGER:START --> and <!-- LEDGER:END -->.

Status emojis recognized: 🟢, 🟡, 🔴, ⚪. We count occurrences inside the
'Falsification Status — by claim' section of each programme file.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

STATUSES = ["🟢", "🟡", "🔴", "⚪"]
HEADERS = ["Supported", "Contested", "Refuted", "Open"]
PROGRAMMES = [
    ("01", "Compression", Path("programmes/01-compression-as-intelligence.md")),
    ("02", "Superposition / LRH", Path("programmes/02-superposition-linear-rep.md")),
    ("03", "Circuits", Path("programmes/03-circuits-and-biology.md")),
    ("04", "ICL-as-Bayes", Path("programmes/04-icl-as-bayes-meta-learning.md")),
    ("05", "Emergence", Path("programmes/05-emergence-and-reasoning.md")),
]
SECTION_RE = re.compile(r"##\s*5\.\s*Falsification Status.*?(?=\n##\s|\Z)", re.DOTALL)

START = "<!-- LEDGER:START -->"
END = "<!-- LEDGER:END -->"


def count_statuses(text: str) -> dict[str, int]:
    m = SECTION_RE.search(text)
    section = m.group(0) if m else ""
    out = {}
    for s in STATUSES:
        out[s] = section.count(s)
    return out


def render_table(counts: list[tuple[str, str, dict[str, int]]]) -> str:
    header = "| Programme | " + " | ".join(f"{e} {h}" for e, h in zip(STATUSES, HEADERS)) + " | Total |"
    sep = "|-----------|" + "|".join(["-" * 15] * 4) + "|-------|"
    rows = []
    totals = {s: 0 for s in STATUSES}
    grand = 0
    for pid, label, counts_d in counts:
        row_total = sum(counts_d.values())
        grand += row_total
        for s in STATUSES:
            totals[s] += counts_d[s]
        rows.append(
            "| " + f"{pid} {label}" + " | " +
            " | ".join(str(counts_d[s]) for s in STATUSES) +
            f" | {row_total} |"
        )
    rows.append(
        "| **Total** | " +
        " | ".join(f"**{totals[s]}**" for s in STATUSES) +
        f" | **{grand}** |"
    )
    return "\n".join([header, sep, *rows])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-readme", action="store_true")
    args = parser.parse_args()

    counts = []
    for pid, label, p in PROGRAMMES:
        if not p.exists():
            print(f"missing {p}; skipping", file=sys.stderr)
            counts.append((pid, label, {s: 0 for s in STATUSES}))
            continue
        counts.append((pid, label, count_statuses(p.read_text(encoding="utf-8"))))

    table = render_table(counts)
    if args.write_readme:
        readme = Path("README.md").read_text(encoding="utf-8")
        if START in readme and END in readme:
            new = re.sub(
                re.escape(START) + r".*?" + re.escape(END),
                f"{START}\n{table}\n{END}",
                readme,
                flags=re.DOTALL,
            )
            Path("README.md").write_text(new, encoding="utf-8")
            print("wrote README.md")
        else:
            print(
                f"Markers {START} / {END} not found in README.md; "
                "add them around the ledger summary table to enable auto-update.",
                file=sys.stderr,
            )
            print(table)
    else:
        print(table)
    return 0


if __name__ == "__main__":
    sys.exit(main())
