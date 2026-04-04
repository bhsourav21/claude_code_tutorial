# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**HookHub** — a read-only discovery platform for open-source Claude Code hooks. Developers can browse community-built hooks sourced from GitHub repositories. MVP scope is display-only: no auth, submissions, or ratings.

The actual application lives in `claude_code_tutorial/` (the nested subdirectory).

## Setup & Running

Virtual environment is at `claude_code_tutorial/.venv` (Python 3.11).

```bash
cd claude_code_tutorial
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

- App: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## Architecture

The app is intentionally minimal — a single-file FastAPI backend with server-side Jinja2 rendering:

- `main.py` — FastAPI app with one route (`GET /`). Reads `data/hooks.json`, extracts unique categories, and renders `templates/index.html`.
- `data/hooks.json` — Static JSON array of hook entries (the data layer for MVP).
- `templates/base.html` + `templates/index.html` — Jinja2 templates using TailwindCSS (CDN). Category filtering is client-side JavaScript (show/hide cards).

### Hook data model

Each entry in `hooks.json` has: `id`, `name`, `description`, `category`, `repo_url`, `author`, `event_types[]`.

Categories: Security, Code Quality, Automation, Observability, Notifications, Other.

## Coding Conventions (from `memory/API/CLAUDE.md`)

- Use `def` for pure functions, `async def` for async operations.
- Type hints on all function signatures; prefer Pydantic models over raw dicts for input validation.
- RORO pattern (Receive an Object, Return an Object).
- Descriptive variable names with auxiliary verbs (`is_active`, `has_permission`).
- Error handling: early returns / guard clauses at function start, happy path last.
- Use `HTTPException` for expected errors; middleware for unexpected ones.
- Prefer functional components; avoid unnecessary classes.
- File structure when expanding: exported router → sub-routes → utilities → static → types.
