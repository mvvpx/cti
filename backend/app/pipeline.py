from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable, List

from .schemas import EvidenceSnippet, Source


@dataclass(frozen=True)
class SeedQuery:
    keyword: str
    sources: List[Source]


def build_seed_urls(query: SeedQuery) -> List[str]:
    static_urls = {
        Source.darkweb: ["https://ahmia.fi/search/?q={keyword}"],
        Source.telegram: [
            "https://t.me/s/{keyword}",
            "https://telegramchannels.me/search?query={keyword}",
        ],
        Source.discord: ["https://disboard.org/search?keyword={keyword}"],
    }

    urls: List[str] = []
    for source in query.sources:
        for template in static_urls.get(source, []):
            urls.append(template.format(keyword=query.keyword))
    return urls


def search_with_selenium(seed_urls: Iterable[str]) -> List[str]:
    # Placeholder for selenium-based search expansion.
    # In production this should: open search engines, extract result links,
    # deduplicate, and enforce allow/deny lists.
    return list(seed_urls)


def extract_snippets(keyword: str, urls: Iterable[str], source: Source) -> List[EvidenceSnippet]:
    now = datetime.now(timezone.utc).isoformat()
    snippets = []
    for url in urls:
        snippets.append(
            EvidenceSnippet(
                source=source,
                url=url,
                title=None,
                snippet=f"Placeholder extract for '{keyword}' from {url}",
                extracted_at=now,
            )
        )
    return snippets


def run_pipeline(keyword: str, sources: List[Source]) -> List[EvidenceSnippet]:
    seed_urls = build_seed_urls(SeedQuery(keyword=keyword, sources=sources))
    discovered_urls = search_with_selenium(seed_urls)

    snippets: List[EvidenceSnippet] = []
    for source in sources:
        source_urls = [url for url in discovered_urls if source.value in url]
        snippets.extend(extract_snippets(keyword, source_urls, source))
    return snippets
