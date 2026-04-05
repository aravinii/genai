# Experiment notebooks (RAG)

These notebooks prototype the **retrieval-augmented** neighborhood research path: build a structured corpus, index it in ChromaDB, and call **Gemini** with a tool that runs embedding search over that index.

They are **not** the same as the production-style agents under [`agents/`](../../agents/); they are a self-contained pipeline for iterating on RAG quality and latency before wiring results into broader evals.

## Suggested order

| Step | Notebook | What it does |
|------|----------|----------------|
| 1 | [**rag_database.ipynb**](rag_database.ipynb) | Uses the **research agent** to generate neighborhood write-ups and saves **`data/rag_database.json`** (sections per bairro). |
| 2 | [**rag_indexing.ipynb**](rag_indexing.ipynb) | Reads `rag_database.json`, embeds with **`GeminiEmbeddingFunction`**, and persists a **Chroma** collection under `data/quarto_research_db/` (see `CHROMA_DB_PATH` / `DB_NAME` in [`utils/config.py`](../../utils/config.py)). |
| 3 | [**rag_agent.ipynb**](rag_agent.ipynb) | Standalone **RAG chat** using `search_neighborhood_context` and `research_agent_v2` prompt — useful for manual QA before comparing against web-search research in evals. |

## Configuration

- Set `GOOGLE_API_KEY` for Gemini and embeddings.
- `sys.path` is pointed at **`real_estate_agent`** (`Path().resolve().parent.parent` from this folder) so `utils.embedding` and `agents.research_agent` import correctly.

## Related

- Side-by-side **metrics and LLM-judge comparison** (RAG vs research-with-search): [`evals/chat_metrics.ipynb`](../../evals/chat_metrics.ipynb) and [`evals/README.md`](../../evals/README.md).
