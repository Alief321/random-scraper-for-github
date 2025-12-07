"""SVG generation utilities"""
import html
import textwrap
from typing import List, Tuple


def wrap_text(text: str, width: int = 40) -> List[str]:
    """Wrap text to multiple lines"""
    return textwrap.wrap(text, width=width)


def escape_html(text: str) -> str:
    """Escape HTML special characters"""
    return html.escape(text)


def generate_svg(
    title: str,
    link: str,
    header_text: str,
    width: int = 680,
    max_lines: int = 6,
    line_height: int = 20,
    padding: int = 20,
    colors: dict = None
) -> str:
    """Generate SVG badge with customizable content
    
    Args:
        title: Main title/content text
        link: Link URL
        header_text: Header text with emoji
        width: SVG width
        max_lines: Maximum lines for title
        line_height: Height of each text line
        padding: Padding around content
        colors: Dict with bg, accent, text_color, link_color keys
    
    Returns:
        SVG string
    """
    if colors is None:
        colors = {
            "bg": "#0f172a",
            "accent": "#ffb86b",
            "text_color": "#e6eef8",
            "link_color": "#9be7ff"
        }
    
    # Escape special chars
    title = escape_html(title)
    link = escape_html(link)
    
    # Wrap title
    wrapped = wrap_text(title, width=40)
    wrapped = wrapped[:max_lines]
    
    # Calculate height
    height = padding * 2 + line_height * (len(wrapped) + 2)
    
    # Build SVG
    lines_svg = []
    y = padding + line_height
    
    # Header
    lines_svg.append(
        f'<text x="{padding}" y="{y}" font-size="18" '
        f'font-family="Segoe UI, Roboto, Arial, sans-serif" font-weight="700" '
        f'fill="{colors["accent"]}">{header_text}</text>'
    )
    y += line_height + 6
    
    # Title lines
    for ln in wrapped:
        lines_svg.append(
            f'<text x="{padding}" y="{y}" font-size="16" '
            f'font-family="Segoe UI, Roboto, Arial, sans-serif" '
            f'fill="{colors["text_color"]}">{ln}</text>'
        )
        y += line_height
    
    # Link
    display_link = link
    if len(display_link) > 80:
        display_link = display_link[:77] + "..."
    y += 6
    lines_svg.append(
        f'<a href="{link}"><text x="{padding}" y="{y}" font-size="13" '
        f'font-family="Segoe UI, Roboto, Arial, sans-serif" '
        f'fill="{colors["link_color"]}">{display_link}</text></a>'
    )
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{header_text}">
  <defs>
    <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000" flood-opacity="0.45"/>
    </filter>
  </defs>
  <rect width="100%" height="100%" rx="12" fill="{colors["bg"]}" filter="url(#shadow)"/>
  <g>
    {"".join(lines_svg)}
  </g>
  <rect x="0" y="{height-28}" width="{width}" height="28" fill-opacity="0"/>
</svg>'''
    return svg
