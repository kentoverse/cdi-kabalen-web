"""Pydantic models for the Kabalen content API."""

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class ContentType(str, Enum):
    HERO = "hero"
    CALLOUT = "callout"
    CARD = "card"
    GALLERY_ITEM = "gallery-item"
    TEXT = "text"


class Section(BaseModel):
    page: str = Field(..., description="Logical page identifier")
    section: str = Field(..., description="Unique section key")
    title: Optional[str] = Field(None, description="Section title")
    subtitle: Optional[str] = Field(None, description="Optional subtitle")
    content: Optional[str] = Field(None, description="Main body copy")
    image: Optional[str] = Field(None, description="Relative asset path")
    display: bool = Field(True, description="Whether the section should be rendered")
    order: int = Field(0, description="Sort order within the page")
    content_type: ContentType = Field(ContentType.TEXT, description="Rendering hint")
    filename: str = Field(..., description="Target HTML file name")


class PageContent(BaseModel):
    filename: str = Field(..., description="HTML file name (e.g. index.html)")
    sections: List[Section] = Field(default_factory=list)


class SiteMap(BaseModel):
    pages: List[PageContent] = Field(default_factory=list)
