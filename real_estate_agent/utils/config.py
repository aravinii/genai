import os
from google import genai
from dotenv import load_dotenv

import os
from pathlib import Path

_base = Path(__file__).resolve().parent   # genai/real_estate_agent/utils
base_dir = _base.parent.parent            # genai/

load_dotenv()

CLIENT = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash"

USER_COLOR = "#D6EAF8"
AGENT_COLOR = "#F9E79F"
FUNCTION_COLOR = "#E5E7E9"

ANSI_USER_COLOR = "\033[93m" 
ANSI_AGENT_COLOR = "\033[94m"
ANSI_FUNCTION_COLOR = "\033[90m"
ANSI_RESET_COLOR = "\033[0m"

MODEL_NAME = "house_price_model.joblib"
MODEL_PATH = base_dir / "pricing_model" / "house_price_model.joblib"

DATA_FOLDER = base_dir / "data"
CONVERSATION_PATH = DATA_FOLDER / "conversations.json"
RAG_DATABASE_PATH = DATA_FOLDER / "rag_database.json"
DB_NAME = "quarto_research_db"
CHROMA_DB_PATH = DATA_FOLDER / DB_NAME
MODEL_EMBEDDING = "models/gemini-embedding-001"

DEFAULT_API_BASE = "http://localhost:8000"