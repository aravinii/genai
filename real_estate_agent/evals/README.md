# Evals

Notebooks for **capturing sample conversations**, **LLM-as-judge scoring**, and **aggregated metrics** (latency, tokens, judge scores). They assume you run from this repo with `GOOGLE_API_KEY` set (see root `.env`) and use JSON under `genai/data/` as configured in [`utils/config.py`](../utils/config.py).

---

### Report (RAG vs Research)

**Generated Markdown report:** [`data/conversation_metrics_report.md`](../../data/conversation_metrics_report.md)

This file summarizes the **RAG Agent vs Research Agent** comparison (LLM-judge scores, latency, tokens, and overview tables). Run [**chat_metrics.ipynb**](chat_metrics.ipynb) to reproduce or refresh the numbers before updating the committed `.md`.

---

## Notebooks

| Notebook | Purpose |
|----------|---------|
| [**chat_sample.ipynb**](chat_sample.ipynb) | Run the full **planner** flow (including pricing server startup), hold multi-turn chats, and **export** histories to `conversations.json` / `conversations_v2.json` for downstream evals. |
| [**chat_evals.ipynb**](chat_evals.ipynb) | Load saved conversations and run **LLM-as-judge** evaluation; writes structured results (e.g. `data/chat_evaluations.json` when configured in the notebook). |
| [**chat_metrics.ipynb**](chat_metrics.ipynb) | **Analyze** exported runs: compare approaches (e.g. Research Agent vs RAG), plots, tables, and alignment with `data/conversation_metrics_report.md` if you regenerate that report from the notebook outputs. |

## Typical workflow

1. Capture or refresh traces with **chat_sample** (pricing API must be reachable if the planner uses the pricing agent).
2. Run **chat_evals** on the JSON snapshot you want to judge.
3. Run **chat_metrics** to summarize latency, token usage, and judge aggregates.

## Paths

These notebooks append `real_estate_agent` to `sys.path` via `Path().resolve().parent` so imports like `agents.*` and `utils.*` resolve the same way as notebooks under [`notebooks/`](../notebooks/).

## Related

- RAG experiments and index building: [`notebooks/experiment/README.md`](../notebooks/experiment/README.md)
- Agent prompts and versioning: [`prompts/README.md`](../prompts/README.md)
