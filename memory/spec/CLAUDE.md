# HookHub — MVP Spec

## Context

HookHub is a discovery platform for open-source Claude Code hooks. Developers who want to automate their Claude Code workflows currently have no central place to browse community-built hooks. HookHub solves this by providing a clean, browsable grid of hooks sourced from GitHub repositories.

MVP scope: **read-only display** of hooks. No auth, no submissions, no ratings.

---

## What Are Claude Hooks (Background)

Claude Code hooks are event-driven shell commands that execute at lifecycle points (PreToolUse, PostToolUse, Stop, Notification, etc.). They're configured in `settings.json` and are a growing ecosystem of community tooling.

---

## Data Model

Each hook entry has:

| Field         | Type     | Description                                      |
|---------------|----------|--------------------------------------------------|
| `id`          | string   | Unique slug (e.g., `parry-injection-detector`)   |
| `name`        | string   | Display name                                     |
| `description` | string   | One- or two-sentence summary                     |
| `category`    | string   | See categories below                             |
| `repo_url`    | string   | Link to GitHub repository                        |
| `author`      | string   | GitHub username                                  |
| `event_types` | string[] | Hook events it uses (PreToolUse, PostToolUse…)   |

### Categories (MVP)

- **Security** — injection detection, secret scanning, command blocking
- **Code Quality** — linting, formatting, test running
- **Automation** — auto-approve flows, workflow shortcuts
- **Observability** — logging, monitoring, multi-agent tracking
- **Notifications** — audio/visual alerts
- **Other**

---

## Seed Data (Known Hooks)

Initial hooks populated in `data/hooks.json`:

1. **karanb192/claude-code-hooks** — Collection of ready-to-use hooks (Automation)
2. **disler/claude-code-hooks-mastery** — Full lifecycle coverage, all 13 events (Observability)
3. **disler/claude-code-hooks-multi-agent-observability** — Real-time multi-agent monitoring (Observability)
4. **decider/claude-hooks** — Clean code enforcement and workflow automation (Code Quality)
5. **hesreallyhim/awesome-claude-code** — Curated list including hooks (Other)

---

## Tech Stack

| Layer      | Choice              | Reason                                   |
|------------|---------------------|------------------------------------------|
| Framework  | FastAPI             | Already set up, Python 3.11              |
| Templating | Jinja2              | Server-side HTML, no JS framework needed |
| Styling    | TailwindCSS (CDN)   | Fast grid layout, no build step          |
| Data       | Static JSON file    | Simplest possible data layer for MVP     |

---

## Pages & Routes

### `GET /` — Main Grid Page

- Displays all hooks in a **responsive card grid** (3 cols desktop, 2 tablet, 1 mobile)
- Each card shows: name, category badge (color-coded), description, author, event type tags, "View on GitHub" link
- Filter bar at top: filter by category (client-side JS, simple show/hide)
- Header: HookHub logo + tagline "Discover open-source Claude Code hooks"

### `GET /hooks/{id}` — Hook Detail Page *(stretch, not in MVP)*

---

## File Structure

```
main.py                  # FastAPI app with routes
data/
  hooks.json             # Seed data (static)
templates/
  base.html              # HTML shell, Tailwind CDN
  index.html             # Grid page (extends base)
spec/
  hookhub-mvp.md         # This spec
```
