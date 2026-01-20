# CTI Platform

This repository contains a starter CTI platform that collects and analyzes keyword-centric data
from dark web sources, Telegram, and Discord. The current implementation is a scaffold that
includes an API service, a web UI, and a pipeline placeholder for Selenium-driven collection.

## Workflow
1. User submits a keyword and selects one or more sources.
2. The API builds seed URLs (static + search engine templates).
3. Selenium expands the link set (placeholder in this scaffold).
4. The system visits each URL, extracts keyword context, and returns structured snippets.
5. The web UI renders the results into intelligence cards.

## Repository layout
- `backend/`: FastAPI service that coordinates the pipeline.
- `frontend/`: Static web UI for keyword search.
- `docs/`: Architecture and workflow notes.

## Quick start
### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

If port 8000 is already in use, run `python -m uvicorn app.main:app --reload --port 8001` and
update the frontend API base URL accordingly. Using `python -m uvicorn` ensures the virtual
environment dependencies are used, which avoids importing system-installed FastAPI/Pydantic.

### Frontend
```bash
cd frontend
python -m http.server 5173
```

Then open `http://localhost:5173` in your browser and confirm the API base URL is pointing at the
backend you started.

## Next steps
- Replace pipeline placeholders with Selenium collectors and content extraction.
- Add storage for evidence and runs.
- Add authentication and analyst workspaces.
