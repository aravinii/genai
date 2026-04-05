# Notebooks

Interactive runs of the **agents** with the same `sys.path` pattern: from a notebook in this folder, `Path().resolve().parent` should be **`real_estate_agent`** so `agents.*` and `utils.*` import correctly.

## Root notebooks

| Notebook | Purpose |
|----------|---------|
| [**planner_agent.ipynb**](planner_agent.ipynb) | Full **planner** chat (starts pricing **FastAPI** via `start_server()`). |
| [**research_agent.ipynb**](research_agent.ipynb) | **Research agent** only (web search). |
| [**pricing_agent.ipynb**](pricing_agent.ipynb) | **Pricing agent** flows and rendering helpers. |

## Subfolders

| Path | Purpose |
|------|---------|
| [**experiment/**](experiment/) | **RAG** pipeline: build `rag_database.json`, Chroma index, standalone RAG chat. See [experiment/README.md](experiment/README.md). |

## Related

- Capture traces and run evals: [`evals/README.md`](../evals/README.md)
- Agent code map: [`agents/README.md`](../agents/README.md)
