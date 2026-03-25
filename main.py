import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="HookHub")
templates = Jinja2Templates(directory="templates")

DATA_DIR = Path(__file__).parent / "data"


def load_hooks() -> list[dict]:
    with open(DATA_DIR / "hooks.json") as f:
        return json.load(f)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    hooks = load_hooks()
    categories = sorted({h["category"] for h in hooks})
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "hooks": hooks, "categories": categories},
    )
