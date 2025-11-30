#!/usr/bin/env python3
"""Convert CSV-authored content into structured JSON and static HTML pages."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

DEFAULT_PAGE_TITLES: Dict[str, str] = {
    "index.html": "Kabalen Toronto – Home",
    "menu.html": "Kabalen – Menu",
    "specials.html": "Kabalen – Daily Specials",
    "gallery.html": "Kabalen – Gallery",
    "about.html": "Kabalen – Our Story",
    "contact.html": "Kabalen – Contact"
}

NAVIGATION_LINKS: Tuple[Tuple[str, str], ...] = (
    ("index.html", "Home"),
    ("menu.html", "Menu"),
    ("specials.html", "Specials"),
    ("gallery.html", "Gallery"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
)


@dataclass
class Section:
    business: str
    page: str
    section: str
    title: str
    subtitle: str
    content: str
    image: str
    display: bool
    order: int
    content_type: str
    filename: str

    @classmethod
    def from_row(cls, row: Dict[str, str]) -> "Section":
        display_value = row.get("display", "true").strip().lower()
        display = display_value in {"1", "true", "yes", "y"}
        order_value = row.get("order", "0").strip()
        try:
            order = int(order_value)
        except ValueError:
            order = 0

        filename = row.get("filename") or f"{row.get('page', '').strip()}.html"

        return cls(
            business=row.get("business", "").strip() or "default",
            page=row.get("page", "").strip(),
            section=row.get("section", "").strip(),
            title=row.get("title", "").strip(),
            subtitle=row.get("subtitle", "").strip(),
            content=row.get("content", "").strip(),
            image=row.get("image", "").strip(),
            display=display,
            order=order,
            content_type=row.get("content_type", "text").strip().lower() or "text",
            filename=filename.strip() if filename else "index.html",
        )


def parse_sections(csv_path: Path, business: Optional[str] = None) -> Dict[str, List[Section]]:
    sections: Dict[str, List[Section]] = {}
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            section = Section.from_row(row)
            if not section.display:
                continue
            if business:
                business_key = business.lower()
                section_key = section.business.lower()
                if section_key not in {business_key, "default"}:
                    continue
            sections.setdefault(section.filename, []).append(section)

    for filename in sections:
        sections[filename].sort(key=lambda item: (item.order, item.section))
    return sections


def serialize_sections(sections: Dict[str, List[Section]], json_path: Path) -> None:
    payload = {
        filename: [asdict(section) for section in section_list]
        for filename, section_list in sections.items()
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def render_sections_html(sections: Iterable[Section]) -> str:
    rendered: List[str] = []
    for section in sections:
        renderer = SECTION_RENDERERS.get(section.content_type, render_text_section)
        rendered.append(renderer(section))
    return "\n".join(rendered)


def render_page(filename: str, sections: Iterable[Section]) -> str:
    sections_list = list(sections)
    if not sections_list:
        return ""
    page_key = filename.lower()
    custom_title = DEFAULT_PAGE_TITLES.get(page_key)
    if not custom_title:
        page_stub = page_key.split(".")[0].replace("-", " ").title()
        custom_title = f"Kabalen – {page_stub}"

    body_html = render_sections_html(sections_list)

    nav_links = " ".join(
        f'<a href="{href}">{label}</a>' for href, label in NAVIGATION_LINKS
    )

    firebase_script = '<script type="module" src="assets/js/firebase-init.js"></script>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{custom_title}</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header>
    <img src="assets/images/kabalen-logo.png" alt="Kabalen Logo" class="logo">
    <nav>{nav_links}</nav>
</header>
{body_html}
<footer>
    <p>© 2025 Kabalen Toronto. All rights reserved.</p>
</footer>
{firebase_script}
</body>
</html>
"""


def render_hero_section(section: Section) -> str:
    image_html = (
        f'<img src="{section.image}" alt="{section.title or section.section}">' if section.image else ""
    )
    subtitle_html = f"<p>{section.subtitle}</p>" if section.subtitle else ""
    content_html = f"<p>{section.content}</p>" if section.content else ""
    return f"""
<section class="hero">
    {image_html}
    <div class="hero-text">
        <h1>{section.title or 'Welcome to Kabalen'}</h1>
        {subtitle_html}
        {content_html}
    </div>
</section>
"""


def render_callout_section(section: Section) -> str:
    content_html = f"<p>{section.content}</p>" if section.content else ""
    button_label = section.title or "Learn More"
    return f"""
<section class="cta">
    <h2>{button_label}</h2>
    {content_html}
</section>
"""


def render_card_section(section: Section) -> str:
    image_html = (
        f'<img src="{section.image}" alt="{section.title}">' if section.image else ""
    )
    subtitle_html = f"<p>{section.subtitle}</p>" if section.subtitle else ""
    content_html = f"<p>{section.content}</p>" if section.content else ""
    return f"""
<section class="card">
    {image_html}
    <h3>{section.title}</h3>
    {subtitle_html}
    {content_html}
</section>
"""


def render_gallery_section(section: Section) -> str:
    image_html = (
        f'<img src="{section.image}" alt="{section.title or section.section}">' if section.image else ""
    )
    caption_title = section.title or "Gallery Highlight"
    caption_body = section.content or section.subtitle
    caption_html = f"<figcaption><p>{caption_body}</p></figcaption>" if caption_body else ""
    return f"""
<section class="gallery-item">
    <figure>
        {image_html}
        <figcaption><h3>{caption_title}</h3>{caption_html}</figcaption>
    </figure>
</section>
"""


def render_text_section(section: Section) -> str:
    subtitle_html = f"<h3>{section.subtitle}</h3>" if section.subtitle else ""
    content_html = f"<p>{section.content}</p>" if section.content else ""
    return f"""
<section class="text-block">
    <h2>{section.title or section.section.title()}</h2>
    {subtitle_html}
    {content_html}
</section>
"""


SECTION_RENDERERS = {
    "hero": render_hero_section,
    "callout": render_callout_section,
    "card": render_card_section,
    "gallery-item": render_gallery_section,
    "gallery": render_gallery_section,
    "text": render_text_section,
}


def build_html_pages(sections: Dict[str, List[Section]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, section_list in sections.items():
        html = render_page(filename, section_list)
        (output_dir / filename).write_text(html, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate static pages and JSON from CSV content.")
    parser.add_argument("csv_path", type=Path, help="Path to the content CSV file.")
    parser.add_argument("--output", type=Path, default=Path("generated-pages"), help="Directory for generated HTML files.")
    parser.add_argument("--json", type=Path, default=Path("build/content.json"), help="Path for aggregated JSON output.")
    parser.add_argument("--business", type=str, default=None, help="Filter rows to a specific business identifier.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    sections = parse_sections(args.csv_path, business=args.business)
    if not sections:
        raise SystemExit("No visible rows found in the CSV. Nothing to generate.")

    serialize_sections(sections, args.json)
    build_html_pages(sections, args.output)


if __name__ == "__main__":
    main()
