# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A FastAPI hello world boilerplate serving as a learning ground for Claude Code . The API is defined entirely in `main.py` with a single `GET /` endpoint returning `{"message": "Hello, World!"}`.

## Environment Setup

Virtual environment is at `.venv` (Python 3.11). Always use it:

```bash
source .venv/bin/activate
```

Install/update dependencies:

```bash
pip install -r requirements.txt
```

## Running the App

```bash
uvicorn main:app --reload
```

API will be available at `http://127.0.0.1:8000`. Interactive docs at `http://127.0.0.1:8000/docs`.

## Dependencies

- `fastapi==0.115.0` — web framework
- `uvicorn[standard]==0.30.6` — ASGI server (includes uvloop, websockets, watchfiles for `--reload`)