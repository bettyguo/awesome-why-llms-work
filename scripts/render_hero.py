"""Render hero.svg — a wide top-of-README banner.

Design:
  - 1600 × 480 (3.33:1) for a top-of-page banner that looks good on both
    GitHub README rendering (which scales) and og:image preview.
  - Dark navy background with a subtle gradient.
  - Big title and subtitle.
  - Right side: five small programme dots with their hue + status pip.
  - Bottom strip: tagline + small stats.
"""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

W, H = 1600, 480


def x(s: str) -> str:
    return html.escape(s, quote=True)


PROGRAMMES = [
    ("01", "Compression",       "#60a5fa", "🟡"),
    ("02", "Superposition",     "#34d399", "🟢"),
    ("03", "Circuits",          "#f87171", "🟢"),
    ("04", "ICL-as-Bayes",      "#a78bfa", "🟡"),
    ("05", "Emergence",         "#fb923c", "🔴"),
]

# cairosvg cannot render colored emoji glyphs (they render as ☐ in the PNG),
# so the SVG draws status indicators as real <circle> shapes.
STATUS_PIP = {
    "🟢": ("#22c55e", "#22c55e"),  # green-500
    "🟡": ("#eab308", "#eab308"),  # yellow-500
    "🔴": ("#ef4444", "#ef4444"),  # red-500
    "⚪": ("#0f172a", "#94a3b8"),  # dark fill (visible on dark bg), slate ring
}


def render_svg() -> str:
    out: list[str] = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" '
        f'font-family="Inter, ui-sans-serif, system-ui, sans-serif">'
    )
    out.append('<defs>')
    out.append(
        '<linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">'
        '<stop offset="0%"   stop-color="#0b1224"/>'
        '<stop offset="55%"  stop-color="#0f172a"/>'
        '<stop offset="100%" stop-color="#111827"/>'
        '</linearGradient>'
        '<radialGradient id="glow" cx="20%" cy="30%" r="60%">'
        '<stop offset="0%"   stop-color="#1e3a8a" stop-opacity="0.55"/>'
        '<stop offset="100%" stop-color="#0f172a" stop-opacity="0"/>'
        '</radialGradient>'
    )
    out.append('</defs>')
    out.append(f'<rect width="{W}" height="{H}" fill="url(#hero-bg)"/>')
    out.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')

    # Big title.
    out.append(
        f'<text x="80" y="160" font-size="68" font-weight="800" '
        f'fill="#f8fafc">Why do LLMs work?</text>'
    )
    # Subtitle.
    out.append(
        f'<text x="80" y="220" font-size="26" font-weight="500" fill="#cbd5e1">'
        f'A falsifiable-hypothesis atlas of five competing research programmes.'
        f'</text>'
    )
    # Tag chips.
    chips = [
        ("five programmes", "#1f2937"),
        ("falsification ledger", "#1f2937"),
        ("42 papers · verified", "#1f2937"),
        ("5 runnable notebooks", "#1f2937"),
        ("CC-BY-4.0", "#1f2937"),
    ]
    cx_ = 80
    for label, fill in chips:
        w = 18 + len(label) * 9
        out.append(
            f'<rect x="{cx_}" y="270" width="{w}" height="34" rx="17" ry="17" '
            f'fill="{fill}" stroke="#334155" stroke-width="1"/>'
        )
        out.append(
            f'<text x="{cx_ + w // 2}" y="293" text-anchor="middle" '
            f'font-size="13" font-weight="600" fill="#e2e8f0">{x(label)}</text>'
        )
        cx_ += w + 12

    # Bottom strip.
    out.append(
        f'<rect x="0" y="{H - 80}" width="{W}" height="80" fill="#020617" '
        f'fill-opacity="0.55"/>'
    )
    out.append(
        f'<text x="80" y="{H - 38}" font-size="15" font-weight="500" '
        f'fill="#94a3b8">'
        f'Compression · Superposition · Circuits · ICL-as-Bayes · Emergence '
        f'— with epistemic status for every claim.'
        f'</text>'
    )

    # Right-side: programme bubbles arranged vertically.
    base_x = W - 360
    base_y = 110
    out.append(
        f'<text x="{base_x}" y="{base_y - 20}" font-size="14" font-weight="700" '
        f'fill="#94a3b8" letter-spacing="2">'
        f'PROGRAMMES'
        f'</text>'
    )
    for i, (pid, name, color, status) in enumerate(PROGRAMMES):
        row_y = base_y + i * 50
        # Color disc.
        out.append(
            f'<circle cx="{base_x + 16}" cy="{row_y}" r="14" fill="{color}"/>'
        )
        out.append(
            f'<text x="{base_x + 16}" y="{row_y + 5}" text-anchor="middle" '
            f'font-size="12" font-weight="800" fill="#0f172a">{x(pid)}</text>'
        )
        # Title + status.
        out.append(
            f'<text x="{base_x + 44}" y="{row_y + 5}" font-size="20" '
            f'font-weight="600" fill="#f1f5f9">{x(name)}</text>'
        )
        pip_fill, pip_stroke = STATUS_PIP[status]
        out.append(
            f'<circle cx="{base_x + 270}" cy="{row_y}" r="9" '
            f'fill="{pip_fill}" stroke="{pip_stroke}" stroke-width="1.5"/>'
        )

    out.append('</svg>')
    return "\n".join(out)


def write_png(svg_path: Path, png_path: Path) -> bool:
    try:
        import cairosvg  # type: ignore
        cairosvg.svg2png(
            url=str(svg_path), write_to=str(png_path),
            output_width=W, output_height=H,
        )
        return True
    except Exception:
        return False


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out-svg", default="hero.svg")
    p.add_argument("--out-png", default="hero.png")
    args = p.parse_args()
    Path(args.out_svg).write_text(render_svg(), encoding="utf-8")
    print(f"wrote {args.out_svg}")
    if write_png(Path(args.out_svg), Path(args.out_png)):
        print(f"wrote {args.out_png}")
    else:
        print("PNG rasterization skipped (install cairosvg).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
