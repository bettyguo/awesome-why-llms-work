"""Render the taxonomy diagram (taxonomy.svg + taxonomy.png).

Visual design:
  - 16:9 aspect (1280×720) for social-preview compatibility.
  - Five programme clusters as color-coded rounded cards.
  - Each card has a header strip in the programme's hue, a body with
    claim nodes, and a small bottom-right status pip.
  - Edges connect programmes with two visual languages:
      solid grey  -> supports / implies
      dashed red  -> in tension with
  - Subtitle, legend, and a small footer with attribution.

The script does not require graphviz; it emits SVG directly. The XML-escape
helper x() protects against < > & " ' inside node labels.

Usage:
    python scripts/render_taxonomy.py [--out-svg taxonomy.svg] [--out-png taxonomy.png]

PNG rasterization is best-effort via cairosvg (preferred) or
svglib+reportlab (fallback). The SVG is the canonical artifact.
"""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path


def x(s: str) -> str:
    """XML-escape a string for safe embedding in SVG text/tspan nodes."""
    return html.escape(s, quote=True)


W, H = 1280, 720  # 16:9

# Programme color identity (color + lighter "tint" for the card body).
PROGRAMMES = {
    "01": {
        "title": "01 — Compression-as-Intelligence",
        "color": "#2563eb",   # blue-600
        "tint":  "#eff6ff",   # blue-50
        "summary": "Capability ≈ linearly tracks bits-per-byte.",
        "status": "contested",
    },
    "02": {
        "title": "02 — Superposition & Linear Representations",
        "color": "#059669",   # emerald-600
        "tint":  "#ecfdf5",   # emerald-50
        "summary": "Models pack n features into d<n dims as linear directions.",
        "status": "supported",
    },
    "03": {
        "title": "03 — Circuits & the Biology of LLMs",
        "color": "#dc2626",   # red-600
        "tint":  "#fef2f2",   # red-50
        "summary": "Small causally-validated sub-graphs implement behaviors.",
        "status": "supported",
    },
    "04": {
        "title": "04 — ICL as Implicit Bayes / Meta-Learning",
        "color": "#7c3aed",   # violet-600
        "tint":  "#f5f3ff",   # violet-50
        "summary": "ICL ≈ Bayesian posterior over latent tasks.",
        "status": "contested",
    },
    "05": {
        "title": "05 — Emergence & Reasoning",
        "color": "#ea580c",   # orange-600
        "tint":  "#fff7ed",   # orange-50
        "summary": "Strong Wei-emergence 🔴; test-time-compute 🟡 alive.",
        "status": "mixed",
    },
}

# Programme card geometry: (x, y, width, height).
LAYOUT = {
    "01": (60,  110, 350, 180),
    "02": (60,  320, 350, 180),
    "03": (470, 110, 350, 180),
    "04": (470, 320, 350, 180),
    "05": (880, 215, 340, 290),
}

# Claim nodes per programme (label, status_emoji).
NODES = {
    "01": [
        ("LMs are lossless compressors of text", "🟢"),
        ("bits-per-byte ≈ linear in benchmark", "🟡"),
        ("Hutter / Solomonoff philosophical anchor", "⚪"),
    ],
    "02": [
        ("Trained nets pack n features into d<n dims", "🟢"),
        ("Features ≈ linear directions in activations", "🟢"),
        ("Cross-family feature universality", "⚪"),
    ],
    "03": [
        ("Induction heads (universal motif)", "🟢"),
        ("IOI / circuit-discovery method", "🟢"),
        ("Circuits explain OOD behavior", "⚪"),
    ],
    "04": [
        ("ICL tracks Bayes-optimal (toy data)", "🟢"),
        ("ICL = portfolio of algorithms", "🟢"),
        ("Bayes-invariant to surface form", "🔴"),
        ("Asymptotic-Bayes equilibrium", "🔴"),
    ],
    "05": [
        ("Strong (Wei) emergence", "🔴"),
        ("Metric-artifact (Schaeffer)", "🟢"),
        ("Test-time-compute scaling axis", "🟡"),
        ("Strict complex-systems emergence", "⚪"),
    ],
}

# Cross-programme edges: (src, dst, label, kind).
EDGES = [
    ("01", "02", "implies (mechanism)", "supports"),
    ("02", "03", "feature graph → circuit graph", "supports"),
    ("03", "04", "induction head ↔ ICL", "supports"),
    ("04", "05", "transient ICL ↔ training-time emergence", "tension"),
    ("01", "05", "reasoning models reopen compression-vs-capability", "tension"),
]


def render_svg() -> str:
    out: list[str] = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" '
        f'font-family="Inter, ui-sans-serif, system-ui, sans-serif">'
    )
    # Defs: gradients, arrow markers, drop shadow.
    out.append('<defs>')
    out.append(
        '<linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">'
        '<stop offset="0%" stop-color="#ffffff"/>'
        '<stop offset="100%" stop-color="#f9fafb"/>'
        '</linearGradient>'
    )
    for pid, p in PROGRAMMES.items():
        out.append(
            f'<linearGradient id="hdr-{pid}" x1="0%" y1="0%" x2="100%" y2="0%">'
            f'<stop offset="0%"   stop-color="{p["color"]}" stop-opacity="0.95"/>'
            f'<stop offset="100%" stop-color="{p["color"]}" stop-opacity="0.75"/>'
            f'</linearGradient>'
        )
    out.append(
        '<filter id="card-shadow" x="-10%" y="-10%" width="120%" height="130%">'
        '<feGaussianBlur in="SourceAlpha" stdDeviation="4"/>'
        '<feOffset dx="0" dy="2" result="off"/>'
        '<feComponentTransfer><feFuncA type="linear" slope="0.18"/></feComponentTransfer>'
        '<feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>'
        '</filter>'
    )
    out.append(
        '<marker id="arrow-supports" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="9" markerHeight="9" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#475569"/>'
        '</marker>'
        '<marker id="arrow-tension" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="9" markerHeight="9" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#b91c1c"/>'
        '</marker>'
    )
    out.append('</defs>')

    # Background.
    out.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')

    # Header: title + subtitle.
    out.append(
        f'<text x="{W // 2}" y="50" text-anchor="middle" font-size="26" '
        f'font-weight="800" fill="#0f172a">'
        f'Why LLMs Work — the Five Programmes Map'
        f'</text>'
    )
    out.append(
        f'<text x="{W // 2}" y="78" text-anchor="middle" font-size="14" '
        f'font-weight="400" fill="#475569">'
        f'A falsifiable-hypothesis atlas of why large language models actually work. '
        f'{x("Status: 🟢 supported · 🟡 contested · 🔴 refuted · ⚪ open")}'
        f'</text>'
    )

    # Edges first so cards sit on top.
    def box_center(pid: str) -> tuple[int, int]:
        bx, by, bw, bh = LAYOUT[pid]
        return bx + bw // 2, by + bh // 2

    for src, dst, label, kind in EDGES:
        x1, y1 = box_center(src)
        x2, y2 = box_center(dst)
        dx, dy = x2 - x1, y2 - y1
        norm = (dx * dx + dy * dy) ** 0.5 or 1.0
        ux, uy = dx / norm, dy / norm
        x1 += int(95 * ux); y1 += int(65 * uy)
        x2 -= int(95 * ux); y2 -= int(65 * uy)
        color = "#475569" if kind == "supports" else "#b91c1c"
        dash = "" if kind == "supports" else 'stroke-dasharray="7,5"'
        marker = (
            'url(#arrow-supports)' if kind == "supports" else 'url(#arrow-tension)'
        )
        out.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="2" {dash} marker-end="{marker}"/>'
        )
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        # White rounded background for the edge label.
        # Approximate width: 7 px per character.
        lw = max(60, len(label) * 7 + 16)
        out.append(
            f'<rect x="{mx - lw // 2}" y="{my - 18}" width="{lw}" height="20" rx="10" ry="10" '
            f'fill="white" stroke="{color}" stroke-width="1"/>'
        )
        out.append(
            f'<text x="{mx}" y="{my - 4}" text-anchor="middle" font-size="10.5" '
            f'fill="{color}" font-weight="600">{x(label)}</text>'
        )

    # Programme cards.
    for pid, (bx, by, bw, bh) in LAYOUT.items():
        p = PROGRAMMES[pid]
        # Card body.
        out.append(
            f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="14" ry="14" '
            f'fill="{p["tint"]}" stroke="{p["color"]}" stroke-width="1.5" '
            f'filter="url(#card-shadow)"/>'
        )
        # Header strip (top 36 px of the card).
        out.append(
            f'<path d="M{bx},{by + 14} a14,14 0 0 1 14,-14 h{bw - 28} '
            f'a14,14 0 0 1 14,14 v22 h{-bw} z" '
            f'fill="url(#hdr-{pid})"/>'
        )
        out.append(
            f'<text x="{bx + 14}" y="{by + 24}" font-size="13.5" '
            f'font-weight="700" fill="#ffffff">'
            f'{x(p["title"])}'
            f'</text>'
        )
        # Summary line under header.
        out.append(
            f'<text x="{bx + 14}" y="{by + 56}" font-size="11" '
            f'fill="#334155" font-style="italic">{x(p["summary"])}</text>'
        )
        # Claim nodes.
        nodes = NODES[pid]
        line_h = 22
        start_y = by + 80
        for i, (label, status) in enumerate(nodes):
            ny = start_y + i * line_h
            out.append(
                f'<text x="{bx + 14}" y="{ny}" font-size="11.5" fill="#0f172a">'
                f'<tspan font-size="13">{x(status)}</tspan>'
                f'<tspan dx="6">{x(label)}</tspan>'
                f'</text>'
            )

    # Footer.
    out.append(
        f'<text x="{W // 2}" y="{H - 18}" text-anchor="middle" font-size="11" '
        f'fill="#94a3b8">'
        f'Solid arrow = supports · Dashed red = in tension · '
        f'42 papers tracked · See README + tracker/falsification-events.md for the ledger'
        f'</text>'
    )

    out.append("</svg>")
    return "\n".join(out)


def write_png(svg_path: Path, png_path: Path) -> bool:
    try:
        import cairosvg  # type: ignore
        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(png_path),
            output_width=W,
            output_height=H,
        )
        return True
    except Exception:
        pass
    try:
        from svglib.svglib import svg2rlg  # type: ignore
        from reportlab.graphics import renderPM  # type: ignore
        drawing = svg2rlg(str(svg_path))
        renderPM.drawToFile(drawing, str(png_path), fmt="PNG")
        return True
    except Exception:
        return False


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out-svg", default="taxonomy.svg")
    p.add_argument("--out-png", default="taxonomy.png")
    args = p.parse_args()

    svg = render_svg()
    Path(args.out_svg).write_text(svg, encoding="utf-8")
    print(f"wrote {args.out_svg}")
    ok = write_png(Path(args.out_svg), Path(args.out_png))
    if ok:
        print(f"wrote {args.out_png}")
    else:
        print(
            "PNG rasterization skipped: install cairosvg or svglib+reportlab to enable. "
            "SVG is the canonical artifact.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
