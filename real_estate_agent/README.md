# Real Estate Agent (Quarto)

Multi-agent conversational system that acts as a **real estate consultant** for selected neighborhoods in São Paulo.

## Agents

The system represents **Quarto**, a real estate agency that only operates in these neighborhoods:

- Santana, Mooca, Brooklin, Vila Mariana, Tatuapé

The **planner agent** talks to the owner with rules and conversation guidelines, understands the intent, routes to the right specialist and keeps context. 

The **research agent** provides qualitative analysis (profile, infrastructure, mobility, perception of value) and can use web search tool. 

The **pricing agent** collects property attributes (bedrooms, bathrooms, area, IPTU, neighborhood, type) and returns an estimated price by calling an ML model served via API.

## Folder structure

| Folder | Purpose |
|--------|---------|
| [**agents/**](agents/) | Orchestrator and specialists: `planner_agent` (router), `research_agent` (neighborhood analysis, optional Google Search), `pricing_agent` (data collection + price API). See [agents/README.md](agents/README.md). |
| [**prompts/**](prompts/) | Versioned system prompts (`.txt`) for each agent. Defines role, rules, and when to use each specialist. See [prompts/README.md](prompts/README.md) for versioning rationale. |
| [**utils/**](utils/) | Shared code: config, prompt loader, render (terminal vs notebook), pricing API client, FastAPI deploy for the price model, `Property` model, and transformers used by the ML pipeline. See [utils/README.md](utils/README.md). |
| [**notebooks/**](notebooks/) | Interactive notebooks to run and test the planner, research agent, and pricing agent in isolation or together. See [notebooks/README.md](notebooks/README.md). |
| [**notebooks/experiment/**](notebooks/experiment/) | RAG pipeline experiments: generate `rag_database.json`, index with Chroma, test RAG chat. See [notebooks/experiment/README.md](notebooks/experiment/README.md). |
| [**evals/**](evals/) | Conversation capture, LLM-as-judge evals, and metrics notebooks. See [evals/README.md](evals/README.md). |