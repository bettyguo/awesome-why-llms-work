"""Render the taxonomy diagram (taxonomy.svg + taxonomy.png).

Five programme clusters as colored boxes; key hypotheses as nodes; arrows for
"implies" and "in tension with" relationships.

Usage:
    python scripts/render_taxonomy.py [--out-svg taxonomy.svg] [--out-png taxonomy.png]

Dependencies (graphviz Python bindings are optional; we emit plain SVG ourselves
so the script works in environments without graphviz):
    Optional: matplotlib for the PNG twin. If unavailable, only SVG is produced.

The diagram is hand-laid-out for legibility at 800px wide and 16:9 aspect.
Regenerate any time the taxonomy changes; commit both SVG and PNG.
"""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path


def x(s: str) -> str:
    """XML-escape a string for safe embedding in SVG text/tspan nodes.

    We use html.escape with quote=True to handle <, >, &, " and '.
    """
    return html.escape(s, quote=True)

# Layout constants (svg coordinates).
W, H = 1280, 720  # 16:9
PROGRAMME_COLOR = {
    "01": "#1f77b4",
    "02": "#2ca02c",
    "03": "#d62728",
    "04": "#9467bd",
    "05": "#ff7f0e",
}
PROGRAMME_TITLE = {
    "01": "01 — Compression-as-Intelligence",
    "02": "02 — Superposition / LRH",
    "03": "03 — Circuits / Biology",
    "04": "04 — ICL as Bayes / Meta-learning",
    "05": "05 — Emergence (and Reasoning)",
}
PROGRAMME_BOX = {
    "01": (60, 80, 300, 200),
    "02": (60, 320, 300, 200),
    "03": (520, 80, 300, 200),
    "04": (520, 320, 300, 200),
    "05": (980, 200, 240, 240),
}
# (programme_id, node label, dx, dy, status_emoji)
NODES = [
    ("01", "bpb ≈ linear in benchmark", 18, 30, "🟡"),
    ("01", "LMs are lossless compressors", 18, 70, "🟢"),
    ("01", "Hutter / Solomonoff anchor", 18, 110, "⚪"),
    ("02", "n features into d<n dimensions", 18, 30, "🟢"),
    ("02", "features ≈ linear directions", 18, 70, "🟢"),
    ("02", "cross-family universality", 18, 110, "⚪"),
    ("03", "induction heads (universal)", 18, 30, "🟢"),
    ("03", "IOI / circuit discovery", 18, 70, "🟢"),
    ("03", "circuits explain OOD", 18, 110, "⚪"),
    ("04", "ICL tracks Bayes-optimal (toy)", 18, 30, "🟢"),
    ("04", "ICL = portfolio of algorithms", 18, 70, "🟢"),
    ("04", "ICL Bayes-optimal on natural data", 18, 110, "🟡"),
    ("04", "asymptotic-Bayes equilibrium", 18, 150, "🔴"),
    ("05", "strong (Wei) emergence", 18, 30, "🔴"),
    ("05", "metric-artifact (Schaeffer)", 18, 70, "🟢"),
    ("05", "test-time-compute scaling", 18, 110, "🟡"),
]
# Edges between programmes: (src_prog, dst_prog, label, kind)
EDGES = [
    ("01", "02", "implies (mechanism)", "supports"),
    ("02", "03", "feature graph → circuit graph", "supports"),
    ("03", "04", "induction head ↔ ICL", "supports"),
    ("04", "05", "transient ICL ↔ training-time emergence", "tension"),
    ("01", "05", "reasoning models reopen compression-capability gap", "tension"),
]


def render_svg() -> str:
    lines = []
    lines.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">'
    )
    lines.append(
        f'<rect width="{W}" height="{H}" fill="#fbfbfb"/>'
        f'<text x="{W // 2}" y="36" text-anchor="middle" font-size="22" font-weight="700">'
        f'Why LLMs Work — Five Programmes Map'
        f'</text>'
    )
    # programme boxes
    for pid, (bx, by, bw, bh) in PROGRAMME_BOX.items():
        color = PROGRAMME_COLOR[pid]
        title = PROGRAMME_TITLE[pid]
        lines.append(
            f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="14" ry="14" '
            f'fill="white" stroke="{color}" stroke-width="2.5"/>'
        )
        lines.append(
            f'<text x="{bx + 12}" y="{by + 22}" font-size="13" font-weight="700" fill="{color}">'
            f'{x(title)}'
            f'</text>'
        )
    # node items
    for pid, label, dx, dy, status in NODES:
        bx, by, _, _ = PROGRAMME_BOX[pid]
        nx, ny = bx + dx, by + dy
        lines.append(
            f'<text x="{nx}" y="{ny}" font-size="11" fill="#222">'
            f'<tspan>{x(status)}</tspan> {x(label)}'
            f'</text>'
        )
    # arrow defs (filled triangles, distinct colors for supports / tension)
    lines.append(
        '<defs>'
        '<marker id="arrow-support" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#444"/>'
        '</marker>'
        '<marker id="arrow-tension" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#b22222"/>'
        '</marker>'
        '</defs>'
    )
    # edges
    def box_center(pid: str) -> tuple[int, int]:
        x, y, w, h = PROGRAMME_BOX[pid]
        return x + w // 2, y + h // 2

    for src, dst, label, kind in EDGES:
        x1, y1 = box_center(src)
        x2, y2 = box_center(dst)
        # offset endpoints to box edges
        dx, dy = x2 - x1, y2 - y1
        norm = (dx ** 2 + dy ** 2) ** 0.5 or 1.0
        ux, uy = dx / norm, dy / norm
        x1 += int(80 * ux); y1 += int(60 * uy)
        x2 -= int(80 * ux); y2 -= int(60 * uy)
        color = "#444" if kind == "supports" else "#b22222"
        marker = f"url(#arrow-{'support' if kind == 'supports' else 'tension'})"
        stroke = "2" if kind == "supports" else "2"
        dash = "" if kind == "supports" else 'stroke-dasharray="6,4"'
        lines.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="{stroke}" {dash} marker-end="{marker}"/>'
        )
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        lines.append(
            f'<text x="{mx}" y="{my - 6}" text-anchor="middle" font-size="10" fill="{color}">'
            f'{x(label)}'
            f'</text>'
        )
    # legend
    lines.append(
        f'<text x="60" y="{H - 40}" font-size="11" fill="#444">'
        f'🟢 supported · 🟡 contested · 🔴 refuted · ⚪ open'
        f'</text>'
        f'<text x="60" y="{H - 22}" font-size="11" fill="#444">'
        f'solid arrow = supports / implies     dashed red arrow = in tension with'
        f'</text>'
    )
    lines.append("</svg>")
    return "\n".join(lines)


def write_png(svg_path: Path, png_path: Path) -> bool:
    """Attempt to render PNG using matplotlib + a minimal SVG-to-PNG path.

    Matplotlib does not natively rasterize SVG; we fall back to embedding the
    SVG and rasterizing via cairosvg if available, or we skip and emit a
    text marker. For CI environments we prefer to rely on the headless `svglib +
    reportlab` or `cairosvg` paths.
    """
    try:
        import cairosvg  # type: ignore
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=1280, output_height=720)
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
            "PNG rasterization skipped: install cairosvg or svglib+reportlab "
            "to enable. SVG is the canonical artifact; PNG is for social previews.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
