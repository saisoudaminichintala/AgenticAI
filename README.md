# LangGraph Agentic Playground

This repository contains hands-on examples for building agentic applications with LangGraph, including:

- LangGraph fundamentals and state management
- Tool-using agents and multi-step workflows
- Agentic RAG and query rewriting patterns
- Debugging and experimentation notebooks

## Project structure

- `1-Langgraph Basics/` - introductory notebooks covering graph construction, chatbots, and state schemas
- `2-Langgraph Advance/` - advanced streaming and workflow patterns
- `3-debugging/` - debugging utilities and example agents
- `4-AgenticRAG/` - retrieval-augmented generation workflows and rewrites

## Setup

1. Create and activate a virtual environment
2. Install dependencies with `pip install -r requirements.txt`
3. Copy your API keys into a local `.env` file (this file is ignored by git)
4. Run the notebooks in order or use the scripts in the repository

## Environment variables

The examples rely on API keys such as:

- `OPENAI_API_KEY`
- `GROQ_API_KEY`
- Optional search or other provider keys used by specific notebooks

## Notes

- Notebook outputs are intentionally cleared from the repository so changes stay focused on code and markdown.
- Keep secrets out of the repository; use a local `.env` file only.
