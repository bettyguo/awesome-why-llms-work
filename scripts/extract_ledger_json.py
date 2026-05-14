"""Extract structured JSON from the five programme files for use by the
GitHub Pages site (docs/).

Output: docs/data/ledger.json with the shape:

{
  "generated_at": "2026-05-14",
  "programmes": [
    {
      "id": "01",
      "title": "Compression-as-Intelligence",
      "hard_core": "...",
      "status_label": "🟡 Contested",
      "color": "#2563eb",
      "claims": [
        {"id": "01-A", "text": "...", "status": "🟢 Supported"},
        ...
      ]
    },
    ...
  ]
}

The extractor reads each programme file, finds the per-claim ledger table
under '## 5. Falsification Status' and pulls (claim_id, claim_text, status).
"""

from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

PROGRAMME_FILES = [
    ("01", "Compression-as-Intelligence",         "#2563eb",
     Path("programmes/01-compression-as-intelligence.md")),
    ("02", "Superposition & Linear Representations", "#059669",
     Path("programmes/02-superposition-linear-rep.md")),
    ("03", "Circuits & the Biology of LLMs",      "#dc2626",
     Path("programmes/03-circuits-and-biology.md")),
    ("04", "ICL as Implicit Bayes / Meta-Learning", "#7c3aed",
     Path("programmes/04-icl-as-bayes-meta-learning.md")),
    ("05", "Emergence and Reasoning",             "#ea580c",
     Path("programmes/05-emergence-and-reasoning.md")),
]

# Match the per-claim ledger row, e.g.
# | 01-A | Some claim text. | 🟢 Supported | Best supporting cite | Best refuting cite |
ROW_RE = re.compile(
    r"^\|\s*(?P<id>\d{2}-[A-Z])\s*\|\s*(?P<text>[^|]+)\|\s*(?P<status>[^|]+)\|"
    r"\s*(?P<support>[^|]+)\|\s*(?P<refute>[^|]+)\|"
)
HARD_CORE_RE = re.compile(
    r"##\s*1\.\s*Hard Core.*?\n(.*?)(?=\n##\s)", re.DOTALL
)
SECTION_RE = re.compile(
    r"##\s*5\.\s*Falsification Status.*?(?=\n##\s|\Z)", re.DOTALL
)


def status_label(status: str) -> str:
    s = status.strip()
    # Normalize multi-line statuses like "🟢 Supported (existence)"
    return s.split("(")[0].strip()


def extract_one(path: Path) -> tuple[str, list[dict]]:
    text = path.read_text(encoding="utf-8")
    # Hard core (first non-empty paragraph after section 1).
    hc_match = HARD_CORE_RE.search(text)
    hard_core = ""
    if hc_match:
        body = hc_match.group(1).strip()
        # Pick the first bold or italic line that looks like the claim
        # ("**...**" or bold block). Fallback to first non-empty paragraph.
        bold_match = re.search(r"\*\*([^*]+)\*\*", body)
        if bold_match:
            hard_core = bold_match.group(1).strip()
        else:
            hard_core = body.split("\n\n")[0].strip()
    # Section 5 with per-claim rows.
    sec_match = SECTION_RE.search(text)
    claims: list[dict] = []
    if sec_match:
        for line in sec_match.group(0).splitlines():
            m = ROW_RE.match(line)
            if not m:
                continue
            claims.append(
                {
                    "id": m.group("id").strip(),
                    "text": m.group("text").strip(),
                    "status": m.group("status").strip(),
                    "status_label": status_label(m.group("status")),
                    "supporting": m.group("support").strip(),
                    "refuting": m.group("refute").strip(),
                }
            )
    return hard_core, claims


def main() -> int:
    out_path = Path("docs/data/ledger.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    programmes = []
    for pid, title, color, fp in PROGRAMME_FILES:
        if not fp.exists():
            print(f"missing {fp}; skipping", file=sys.stderr)
            continue
        hard_core, claims = extract_one(fp)
        programmes.append(
            {
                "id": pid,
                "title": title,
                "color": color,
                "file": fp.as_posix(),
                "hard_core": hard_core,
                "claims": claims,
            }
        )

    payload = {
        "generated_at": datetime.date.today().isoformat(),
        "programmes": programmes,
        "totals": {
            "programmes": len(programmes),
            "claims": sum(len(p["claims"]) for p in programmes),
        },
    }
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    n_claims = payload["totals"]["claims"]
    print(f"wrote {out_path} ({payload['totals']['programmes']} programmes, {n_claims} claims)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
