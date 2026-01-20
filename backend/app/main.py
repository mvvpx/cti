from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from .pipeline import run_pipeline
from .schemas import SearchRequest, SearchResponse

app = FastAPI(title="CTI Platform API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_dir = Path(__file__).resolve().parents[2] / "frontend"
if frontend_dir.exists():
    app.mount("/ui", StaticFiles(directory=frontend_dir, html=True), name="ui")


@app.get("/ui")
def ui_root() -> RedirectResponse:
    return RedirectResponse(url="/ui/")


@app.get("/")
def root() -> dict:
    return {
        "service": "cti-platform",
        "status": "ok",
        "routes": {
            "health": "/health",
            "search": "/search",
            "docs": "/docs",
        },
    }


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    snippets = run_pipeline(request.keyword, request.sources)
    return SearchResponse(
        keyword=request.keyword,
        sources=request.sources,
        total_urls=len(snippets),
        snippets=snippets[: request.max_results],
    )
