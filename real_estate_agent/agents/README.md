# Agents

Python entry points for **Quarto**’s multi-agent chat: one **planner** orchestrates user turns and calls **specialists** via Gemini function calling. System instructions live under [`prompts/`](../prompts/) (see [prompts/README.md](../prompts/README.md)).

## Modules

| Module | Role |
|--------|------|
| [**planner_agent.py**](planner_agent.py) | Main loop: loads `planner_agent_v2`, exposes **research** (web **or** RAG) and **pricing** as tools, tracks tokens/latency/history for eval exports. |
| [**research_agent.py**](research_agent.py) | Single-shot neighborhood report using `research_agent_v1` and **Google Search**. |
| [**rag_agent.py**](rag_agent.py) | Same UX as research, but **retrieval** via `search_neighborhood_context` (Chroma + embeddings) and `research_agent_v2`. |
| [**pricing_agent.py**](pricing_agent.py) | Conversational collection of `Property` fields, then **`predict_price`** against the local pricing API. |

## Planner modes

- **Default:** `planner_agent(..., rag=False)` wires **research_agent** (web search).
- **RAG:** `planner_agent(..., rag=True)` wires **rag_agent** instead, for comparisons and lower-latency offline context (after indexing — see [notebooks/experiment/README.md](../notebooks/experiment/README.md)).

## Related

- Runbooks and metrics: [`evals/README.md`](../evals/README.md)
- Shared types, API, and embeddings: [`utils/README.md`](../utils/README.md)
