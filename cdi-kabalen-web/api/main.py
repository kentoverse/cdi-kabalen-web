"""FastAPI application exposing CSV-authored content as JSON."""

from __future__ import annotations

from pathlib import Path
from fastapi import Depends, FastAPI, HTTPException

from .content_loader import ContentLoader
from .models import PageContent, Section, SiteMap

CSV_PATH = Path(__file__).resolve().parent.parent / "content" / "content-template.csv"
loader = ContentLoader(CSV_PATH)
app = FastAPI(title="Kabalen Content API", version="0.1.0")


def normalize_filename(page: str) -> str:
    page = page.strip()
    if not page:
        return "index.html"
    if not page.endswith(".html"):
        return f"{page}.html"
    return page


def get_loader() -> ContentLoader:
    return loader


@app.get("/healthz", tags=["meta"])  # pragma: no cover - trivial endpoint
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/pages", response_model=SiteMap, tags=["content"])
async def list_pages(content_loader: ContentLoader = Depends(get_loader)) -> SiteMap:
    pages = content_loader.get_site_map()
    return SiteMap(pages=pages)


@app.get("/pages/{page}", response_model=PageContent, tags=["content"])
async def get_page(page: str, content_loader: ContentLoader = Depends(get_loader)) -> PageContent:
    filename = normalize_filename(page)
    return content_loader.get_page(filename)


@app.get("/pages/{page}/sections/{section}", response_model=Section, tags=["content"])
async def get_section(page: str, section: str, content_loader: ContentLoader = Depends(get_loader)) -> Section:
    filename = normalize_filename(page)
    page_content = content_loader.get_page(filename)
    for item in page_content.sections:
        if item.section == section:
            return item
    raise HTTPException(status_code=404, detail="Section not found")
