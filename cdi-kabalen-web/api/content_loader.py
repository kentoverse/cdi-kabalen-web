"""Utilities for loading CSV-authored content into structured models."""

from __future__ import annotations

import csv
import threading
from pathlib import Path
from typing import Dict, List

from fastapi import HTTPException, status

from .models import ContentType, PageContent, Section


DISPLAY_TRUE = {"1", "true", "yes", "y"}


class ContentLoader:
    """Lazy CSV loader with caching and file change detection."""

    def __init__(self, csv_path: Path) -> None:
        self._csv_path = csv_path
        self._lock = threading.Lock()
        self._cache: Dict[str, PageContent] = {}
        self._last_mtime: float | None = None

    def _row_to_section(self, row: Dict[str, str]) -> Section | None:
        display_raw = row.get("display", "true").strip().lower()
        if display_raw and display_raw not in DISPLAY_TRUE:
            return None

        order_raw = row.get("order", "0").strip()
        try:
            order = int(order_raw)
        except ValueError:
            order = 0

        content_type_raw = row.get("content_type", "text").strip().lower() or "text"
        try:
            content_type = ContentType(content_type_raw)
        except ValueError:
            content_type = ContentType.TEXT

        filename = row.get("filename") or f"{row.get('page', '').strip()}.html"

        safe_filename = filename.strip() if filename else "index.html"

        page_key = row.get("page", "").strip()
        section_key = row.get("section", "").strip()
        if not section_key:
            return None

        return Section(
            page=page_key,
            section=section_key,
            title=row.get("title") or None,
            subtitle=row.get("subtitle") or None,
            content=row.get("content") or None,
            image=row.get("image") or None,
            display=True,
            order=order,
            content_type=content_type,
            filename=safe_filename,
        )

    def _parse_csv(self) -> Dict[str, PageContent]:
        if not self._csv_path.exists():
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Missing content CSV at {self._csv_path}",
            )

        sections_by_file: Dict[str, List[Section]] = {}
        with self._csv_path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                section = self._row_to_section(row)
                if not section:
                    continue
                sections_by_file.setdefault(section.filename, []).append(section)

        for section_list in sections_by_file.values():
            section_list.sort(key=lambda item: (item.order, item.section))

        return {
            filename: PageContent(filename=filename, sections=section_list)
            for filename, section_list in sections_by_file.items()
        }

    def _refresh_cache(self) -> None:
        with self._lock:
            try:
                mtime = self._csv_path.stat().st_mtime
            except FileNotFoundError as exc:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Missing content CSV at {self._csv_path}",
                ) from exc
            if self._last_mtime and mtime <= self._last_mtime:
                return
            self._cache = self._parse_csv()
            self._last_mtime = mtime

    def get_page(self, filename: str) -> PageContent:
        self._refresh_cache()
        page = self._cache.get(filename)
        if not page:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page not found")
        return page

    def get_site_map(self) -> List[PageContent]:
        self._refresh_cache()
        return sorted(self._cache.values(), key=lambda page: page.filename)
