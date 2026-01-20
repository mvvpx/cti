from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Source(str, Enum):
    darkweb = "darkweb"
    telegram = "telegram"
    discord = "discord"


class SearchRequest(BaseModel):
    keyword: str = Field(..., min_length=2, max_length=200)
    sources: List[Source] = Field(..., min_items=1)
    max_results: int = Field(20, ge=1, le=200)


class EvidenceSnippet(BaseModel):
    source: Source
    url: str
    title: Optional[str]
    snippet: str
    extracted_at: str


class SearchResponse(BaseModel):
    keyword: str
    sources: List[Source]
    total_urls: int
    snippets: List[EvidenceSnippet]
