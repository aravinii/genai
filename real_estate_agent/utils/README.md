# Utils

Shared library code for **agents**, **notebooks**, and **evals**. Paths and API keys are centralized in **`config`** (repo-root `data/`, Chroma location, Gemini client, pricing model path).

## Modules

| Module | Purpose |
|--------|---------|
| [**config.py**](config.py) | `CLIENT`, `MODEL`, colors, `DATA_FOLDER`, conversation and RAG file paths, Chroma `DB_NAME` / `CHROMA_DB_PATH`, embedding model id, pricing API base URL. |
| [**load_prompt.py**](load_prompt.py) | Load `prompts/<name>.txt` relative to `real_estate_agent`. |
| [**render.py**](render.py) | **`render_block`**: notebook HTML bubbles vs terminal ANSI for USER / AGENT / FUNCTION. |
| [**format.py**](format.py) | **`format_judge_conversation`**, **`parse_json_output`** (fenced JSON) for eval notebooks. |
| [**property.py**](property.py) | Pydantic **`Property`** model and helpers used by the pricing agent. |
| [**pricing.py**](pricing.py) | **`predict_price`**: HTTP POST to the pricing service `/predict`. |
| [**pricing_model_deploy.py**](pricing_model_deploy.py) | FastAPI app + **`start_server`** (background thread, port check) loading the joblib model via **`transformers`**. |
| [**transformers.py**](transformers.py) | **`clip_transformer`**, **`zero_to_nan`** — sklearn pipeline pieces for the deployed model. |
| [**embedding.py**](embedding.py) | **`GeminiEmbeddingFunction`** (Chroma), **`search_neighborhood_context`** (persistent client + neighborhood filter). |

## Related

- Agent orchestration: [`agents/README.md`](../agents/README.md)
- RAG indexing workflow: [`notebooks/experiment/README.md`](../notebooks/experiment/README.md)
