# CTI Platform Architecture

## Goals
- Collect CTI signals from dark web, Telegram, and Discord.
- Extract keyword-centric context into structured intelligence cards.
- Present results in a lightweight web UI.

## Components
1. **Web UI** (`frontend/`)
   - Keyword input, source selection, and result list.
   - Communicates with the API via JSON.
2. **API Service** (`backend/`)
   - Orchestrates the collection pipeline.
   - Normalizes and returns snippets to the UI.
3. **Collection Pipeline** (`backend/app/pipeline.py`)
   - Build seed URLs from static lists.
   - Expand links with Selenium-backed search.
   - Fetch and extract keyword snippets.
4. **Storage (Future)**
   - Persist evidence, runs, and analyst notes (e.g., Postgres + object storage).

## Data Flow
1. User submits a keyword + sources.
2. API builds seed URLs + expands them with Selenium.
3. Each URL is visited and parsed to extract context.
4. Results are normalized into evidence snippets and returned to UI.
