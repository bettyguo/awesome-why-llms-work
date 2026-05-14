"""Render the taxonomy diagram (taxonomy.svg + taxonomy.png).

Visual design:
  - 16:9 aspect (1600×900) for social-preview compatibility and breathing room.
  - Five programme clusters as color-coded rounded cards in a 2×2 + 1 layout:
      01 top-left      03 top-center
      02 bot-left      04 bot-center      05 right (vertically centered)
  - Edges connect programmes with two visual languages:
      solid grey  -> supports / implies
      dashed red  -> in tension with
    Edge endpoints are computed from the actual box rectangles (not heuristic
    pixel offsets), so labels always land in the *gaps* between cards.
  - The long 01↔05 tension edge is drawn as a cubic-bezier arc *over* card 03
    so it never crosses a card body.
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


W, H = 1600, 900  # 16:9

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
        "summary": "Strong Wei-emergence refuted; test-time-compute alive.",
        "status": "mixed",
    },
}

# Programme card geometry: (x, y, width, height).
# 2×2 grid on the left + a wider card on the right, all comfortably spaced.
LAYOUT = {
    "01": (60,   160, 400, 240),
    "02": (60,   500, 400, 240),
    "03": (530,  160, 400, 240),
    "04": (530,  500, 400, 240),
    "05": (1160, 310, 380, 280),
}

# Claim nodes per programme (label, status_emoji).
NODES = {
    "01": [
        ("LMs are lossless compressors of text", "🟢"),
        ("bits-per-byte ≈ linear in benchmark", "🟡"),
        ("Hutter / Solomonoff anchor", "⚪"),
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
        ("Test-time-compute scaling", "🟡"),
        ("Strict complex-systems emergence", "⚪"),
    ],
}

# Status pip styling for the SVG circles that replace emoji glyphs.
# (fill, stroke). cairosvg cannot render colored emoji, so we use real shapes.
STATUS_PIP = {
    "🟢": ("#16a34a", "#16a34a"),  # green-600
    "🟡": ("#eab308", "#eab308"),  # yellow-500
    "🔴": ("#dc2626", "#dc2626"),  # red-600
    "⚪": ("#ffffff", "#94a3b8"),  # white fill, slate stroke (hollow look)
}

# Cross-programme edges: (src, dst, label, kind, route).
#   kind:  "supports" (solid grey)  |  "tension" (dashed red)
#   route: "straight" (line between box edges)
#          "arc"      (cubic bezier from src-top over the top to dst-top)
EDGES = [
    ("01", "02", "implies mechanism",     "supports", "straight"),
    ("02", "03", "features → circuits",   "supports", "straight"),
    ("03", "04", "induction ↔ ICL",       "supports", "straight"),
    ("04", "05", "transient ↔ emergence", "tension",  "straight"),
    ("01", "05", "reasoning ↔ compression", "tension", "arc"),
]


def box_center(pid: str) -> tuple[int, int]:
    bx, by, bw, bh = LAYOUT[pid]
    return bx + bw // 2, by + bh // 2


def box_top(pid: str) -> tuple[int, int]:
    bx, by, bw, _bh = LAYOUT[pid]
    return bx + bw // 2, by


def line_endpoints(
    src: str, dst: str, pad: int = 8
) -> tuple[int, int, int, int]:
    """Return (x1,y1,x2,y2) where a straight edge between src and dst boxes
    exits/enters the respective box rectangles, with a small `pad` so the
    arrow head sits clear of the card border."""
    cx1, cy1 = box_center(src)
    cx2, cy2 = box_center(dst)
    dx, dy = cx2 - cx1, cy2 - cy1
    norm = (dx * dx + dy * dy) ** 0.5 or 1.0
    ux, uy = dx / norm, dy / norm

    def edge_t(pid: str) -> float:
        _, _, bw, bh = LAYOUT[pid]
        half_w, half_h = bw / 2, bh / 2
        tx = half_w / abs(ux) if ux != 0 else 1e9
        ty = half_h / abs(uy) if uy != 0 else 1e9
        return min(tx, ty)

    t1 = edge_t(src) + pad
    t2 = edge_t(dst) + pad
    x1 = int(cx1 + t1 * ux)
    y1 = int(cy1 + t1 * uy)
    x2 = int(cx2 - t2 * ux)
    y2 = int(cy2 - t2 * uy)
    return x1, y1, x2, y2


# ---- shared layout math (used by both render_svg() and validate_layout()) ----

ARC_APEX_Y = 60      # y of the cubic-bezier control points for "arc" routes
ARC_END_PAD = 8      # gap above source/dest card for arc start/end


def label_width(label: str) -> int:
    """Match the width formula used by draw_label() inside render_svg()."""
    return max(70, int(len(label) * 7.5) + 20)


def edge_label_center(
    src: str, dst: str, route: str
) -> tuple[int, int]:
    """Return (mx, my) where the edge's white pill label is centered.
    Mirrors the math the renderer uses for both straight and arc routes."""
    if route == "arc":
        sx, sy = box_top(src)
        ex, ey = box_top(dst)
        sy_out = sy - ARC_END_PAD
        ey_in = ey - ARC_END_PAD
        mx = (sx + ex) // 2
        my = int((sy_out + ey_in) / 8 + 0.75 * ARC_APEX_Y)
        return mx, my
    x1, y1, x2, y2 = line_endpoints(src, dst, pad=8)
    return (x1 + x2) // 2, (y1 + y2) // 2


def edge_label_rect(
    src: str, dst: str, label: str, route: str
) -> tuple[int, int, int, int]:
    """(x, y, w, h) of the rounded-rect label background, matching draw_label()."""
    mx, my = edge_label_center(src, dst, route)
    lw = label_width(label)
    return (mx - lw // 2, my - 12, lw, 22)


def _rects_overlap(
    a: tuple[int, int, int, int], b: tuple[int, int, int, int]
) -> bool:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return not (ax + aw <= bx or bx + bw <= ax or ay + ah <= by or by + bh <= ay)


def validate_layout() -> list[str]:
    """Return a list of human-readable overlap warnings.

    A warning is produced for every (edge_label, card) pair whose rectangles
    intersect. The original layout bug (label "transient ICL ↔ training-time
    emergence" sitting on card 04 / card 05) would be caught here.
    """
    warnings: list[str] = []
    for src, dst, label, _kind, route in EDGES:
        lr = edge_label_rect(src, dst, label, route)
        for pid, (bx, by, bw, bh) in LAYOUT.items():
            if _rects_overlap(lr, (bx, by, bw, bh)):
                warnings.append(
                    f"edge {src}->{dst} label {label!r} (rect {lr}) "
                    f"overlaps card {pid} (rect {(bx, by, bw, bh)})"
                )
    return warnings


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
        f'<text x="{W // 2}" y="44" text-anchor="middle" font-size="30" '
        f'font-weight="800" fill="#0f172a">'
        f'Why LLMs Work — the Five Programmes Map'
        f'</text>'
    )
    out.append(
        f'<text x="{W // 2}" y="74" text-anchor="middle" font-size="15" '
        f'font-weight="400" fill="#475569">'
        f'A falsifiable-hypothesis atlas of why large language models actually work.'
        f'</text>'
    )

    def draw_label(mx: int, my: int, label: str, color: str) -> None:
        # Width formula must match label_width() so validate_layout() sees the
        # same rect the renderer draws.
        lw = label_width(label)
        out.append(
            f'<rect x="{mx - lw // 2}" y="{my - 12}" width="{lw}" height="22" '
            f'rx="11" ry="11" fill="white" stroke="{color}" stroke-width="1"/>'
        )
        out.append(
            f'<text x="{mx}" y="{my + 4}" text-anchor="middle" font-size="12" '
            f'fill="{color}" font-weight="600">{x(label)}</text>'
        )

    # Edges first so cards sit on top of any line-end leakage.
    for src, dst, label, kind, route in EDGES:
        color = "#475569" if kind == "supports" else "#b91c1c"
        dash = "" if kind == "supports" else 'stroke-dasharray="7,5"'
        marker = (
            'url(#arrow-supports)' if kind == "supports" else 'url(#arrow-tension)'
        )

        if route == "arc":
            # Cubic bezier arcing over the top: leave src from its top edge,
            # enter dst at its top edge, control points lifted to y=ARC_APEX_Y.
            sx, sy = box_top(src)
            ex, ey = box_top(dst)
            sy_out = sy - ARC_END_PAD
            ey_in = ey - ARC_END_PAD
            out.append(
                f'<path d="M {sx} {sy_out} C {sx} {ARC_APEX_Y} '
                f'{ex} {ARC_APEX_Y} {ex} {ey_in}" '
                f'fill="none" stroke="{color}" stroke-width="2" {dash} '
                f'marker-end="{marker}"/>'
            )
        else:
            x1, y1, x2, y2 = line_endpoints(src, dst, pad=8)
            out.append(
                f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                f'stroke="{color}" stroke-width="2" {dash} marker-end="{marker}"/>'
            )

        mx, my = edge_label_center(src, dst, route)
        draw_label(mx, my, label, color)

    # Programme cards.
    for pid, (bx, by, bw, bh) in LAYOUT.items():
        p = PROGRAMMES[pid]
        # Card body.
        out.append(
            f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="14" ry="14" '
            f'fill="{p["tint"]}" stroke="{p["color"]}" stroke-width="1.5" '
            f'filter="url(#card-shadow)"/>'
        )
        # Header strip (top 40 px of the card).
        out.append(
            f'<path d="M{bx},{by + 14} a14,14 0 0 1 14,-14 h{bw - 28} '
            f'a14,14 0 0 1 14,14 v26 h{-bw} z" '
            f'fill="url(#hdr-{pid})"/>'
        )
        out.append(
            f'<text x="{bx + 16}" y="{by + 26}" font-size="15" '
            f'font-weight="700" fill="#ffffff">'
            f'{x(p["title"])}'
            f'</text>'
        )
        # Summary line under header.
        out.append(
            f'<text x="{bx + 16}" y="{by + 62}" font-size="12.5" '
            f'fill="#334155" font-style="italic">{x(p["summary"])}</text>'
        )
        # Claim nodes.
        nodes = NODES[pid]
        line_h = 26
        start_y = by + 92
        for i, (label, status) in enumerate(nodes):
            ny = start_y + i * line_h
            fill, stroke = STATUS_PIP[status]
            # Status pip: small SVG circle (renders in cairo, unlike emoji).
            out.append(
                f'<circle cx="{bx + 22}" cy="{ny - 4}" r="6" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
            )
            out.append(
                f'<text x="{bx + 36}" y="{ny}" font-size="13" fill="#0f172a">'
                f'{x(label)}'
                f'</text>'
            )

    # Footer: legend row (with real SVG circles) then attribution line.
    legend_items = [
        ("🟢", "supported"),
        ("🟡", "contested"),
        ("🔴", "refuted"),
        ("⚪", "open"),
    ]
    char_w = 7
    pip_r = 6
    gap_after_pip = 8
    gap_between_groups = 22
    group_widths = [
        2 * pip_r + gap_after_pip + len(label) * char_w
        for _, label in legend_items
    ]
    legend_total = sum(group_widths) + gap_between_groups * (len(legend_items) - 1)
    legend_y = H - 50
    cur_x = W // 2 - legend_total // 2
    for (status, label), gw in zip(legend_items, group_widths):
        fill, stroke = STATUS_PIP[status]
        out.append(
            f'<circle cx="{cur_x + pip_r}" cy="{legend_y - 4}" r="{pip_r}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
        )
        out.append(
            f'<text x="{cur_x + 2 * pip_r + gap_after_pip}" y="{legend_y}" '
            f'font-size="13" fill="#475569">{x(label)}</text>'
        )
        cur_x += gw + gap_between_groups

    out.append(
        f'<text x="{W // 2}" y="{H - 24}" text-anchor="middle" font-size="13" '
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
    p.add_argument(
        "--strict",
        action="store_true",
        help="exit non-zero if any edge label overlaps a card rectangle",
    )
    args = p.parse_args()

    warnings = validate_layout()
    for w in warnings:
        print(f"layout warning: {w}", file=sys.stderr)
    if warnings and args.strict:
        print(
            f"layout check failed: {len(warnings)} overlap(s). "
            f"Adjust LAYOUT, shorten labels, or change edge route.",
            file=sys.stderr,
        )
        return 2

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
