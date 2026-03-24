# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A FastAPI hello world boilerplate serving as a learning ground for Claude Code. The entire API lives in `main.py` — a single `GET /` endpoint returning `{"message": "Hello, World!"}`.

## Setup & Running

Virtual environment is at `.venv` (Python 3.11).

```bash
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

- API: `http://127.0.0.1:8000`
- Interactive docs (Swagger UI): `http://127.0.0.1:8000/docs`
- OpenAPI schema: `http://127.0.0.1:8000/openapi.json`