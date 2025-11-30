from __future__ import annotations

import argparse
import csv
import html
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List

IMAGE_CONTENT_TYPES = {"image", "gallery", "gallery-item"}


@dataclass(order=True)
class ContentBlock:
    sort_index: int = field(init=False, repr=False)
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

    def __post_init__(self) -> None:
        self.sort_index = self.order
        if not self.filename:
            self.filename = f"{self.page}.html"
        if not self.content_type:
            self.content_type = "section"
        self.page = self.page.strip() if self.page else ""
        self.section = self.section.strip() if self.section else ""


def parse_bool(value: str) -> bool:
    if isinstance(value, bool):
        return value
    lowered = (value or "").strip().lower()
    return lowered in {"true", "1", "yes", "y"}


def load_blocks(csv_path: Path) -> List[ContentBlock]:
    blocks: List[ContentBlock] = []
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if not row:
                continue

            display = parse_bool(row.get("display", "true"))
            if not display:
                continue

            try:
                order_value = int(row.get("order", "999"))
            except ValueError:
                order_value = 999

            block = ContentBlock(
                page=(row.get("page") or "").strip(),
                section=(row.get("section") or "").strip(),
                title=(row.get("title") or "").strip(),
                subtitle=(row.get("subtitle") or "").strip(),
                content=row.get("content") or "",
                image=(row.get("image") or "").strip(),
                display=True,
                order=order_value,
                content_type=(row.get("content_type") or "").strip(),
                filename=(row.get("filename") or "").strip(),
            )
            blocks.append(block)
    return blocks


def group_blocks_by_page(blocks: Iterable[ContentBlock]) -> Dict[str, List[ContentBlock]]:
    grouped: Dict[str, List[ContentBlock]] = {}
    for block in blocks:
        if not block.page:
            continue
        grouped.setdefault(block.page, []).append(block)
    for items in grouped.values():
        items.sort()
    return grouped


def ensure_image_placeholders(page: str, blocks: List[ContentBlock], max_slots: int) -> None:
    image_blocks = [b for b in blocks if b.content_type in IMAGE_CONTENT_TYPES]
    if not image_blocks:
        return

    needed = max(0, max_slots - len(image_blocks))
    if needed == 0:
        return

    starting_order = (blocks[-1].order if blocks else 0) + 1
    for index in range(needed):
        placeholder = ContentBlock(
            page=page,
            section=f"placeholder-{index + 1}",
            title="",
            subtitle="",
            content="",
            image="",
            display=True,
            order=starting_order + index,
            content_type="image-placeholder",
            filename=f"{page}.html",
        )
        blocks.append(placeholder)
    blocks.sort()


def render_block(block: ContentBlock) -> str:
    section_id = block.section or block.content_type or "section"
    classes = ["content-block", f"content-block--{block.content_type or 'default'}"]
    html_parts = [f'<section id="{section_id}" class="{" ".join(classes)}">']

    if block.title:
        html_parts.append(f"  <h2>{html.escape(block.title)}</h2>")
    if block.subtitle:
        html_parts.append(f"  <h3>{html.escape(block.subtitle)}</h3>")

    if block.image:
        html_parts.append(
            "  <figure>"
            f"<img src=\"{html.escape(block.image)}\" alt=\"{html.escape(block.title or block.section or 'Kabalen dish')}\">"
            "</figure>"
        )
    elif block.content_type == "image-placeholder":
        html_parts.append(
            "  <figure class=\"placeholder\">"
            "<div class=\"placeholder__frame\" aria-hidden=\"true\"></div>"
            "</figure>"
        )

    if block.content:
        paragraphs = [p.strip() for p in block.content.split("\n\n") if p.strip()]
        for paragraph in paragraphs:
            html_parts.append(f"  <p>{html.escape(paragraph)}</p>")

    html_parts.append("</section>")
    return "\n".join(html_parts)


def render_page_html(page: str, blocks: List[ContentBlock]) -> str:
    body_sections = "\n\n".join(render_block(block) for block in blocks)
    return (
        "<!DOCTYPE html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        f"  <title>Kabalen Toronto — {html.escape(page.title())}</title>\n"
        "  <link rel=\"stylesheet\" href=\"assets/css/style.css\">\n"
        "</head>\n"
        "<body>\n"
        f"  <main id=\"{html.escape(page)}\">\n"
        f"{body_sections}\n"
        "  </main>\n"
        "</body>\n"
        "</html>\n"
    )


def write_page(output_dir: Path, filename: str, html_content: str) -> None:
    target = output_dir / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html_content, encoding="utf-8")


def generate_pages(csv_path: Path, output_dir: Path, max_image_slots: int) -> None:
    blocks = load_blocks(csv_path)
    grouped = group_blocks_by_page(blocks)

    for page, page_blocks in grouped.items():
        ensure_image_placeholders(page, page_blocks, max_image_slots)
        filename = page_blocks[0].filename if page_blocks else f"{page}.html"
        html_content = render_page_html(page, page_blocks)
        write_page(output_dir, filename, html_content)
        print(f"Generated {filename} with {len(page_blocks)} sections.")


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate static HTML pages for Kabalen from a CSV content source.",
    )
    parser.add_argument(
        "csv",
        nargs="?",
        default="content/content-template.csv",
        type=Path,
        help="Path to the CSV file containing content definitions.",
    )
    parser.add_argument(
        "--output",
        default="generated-pages",
        type=Path,
        help="Directory where generated HTML files will be written.",
    )
    parser.add_argument(
        "--max-image-slots",
        default=10,
        type=int,
        help="Maximum number of image slots per page (placeholders will be added if fewer exist).",
    )
    return parser


def main() -> None:
    parser = build_argument_parser()
    args = parser.parse_args()

    if not args.csv.exists():
        raise FileNotFoundError(f"CSV file not found: {args.csv}")

    generate_pages(args.csv, args.output, args.max_image_slots)


if __name__ == "__main__":
    main()
