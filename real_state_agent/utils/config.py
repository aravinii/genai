import os
from google import genai
from dotenv import load_dotenv
from pathlib import Path

base_dir = Path.cwd().parent.parent
load_dotenv()

CLIENT = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash"
USER_COLOR = "#D6EAF8"
AGENT_COLOR = "#F9E79F"
FUNCTION_COLOR = "#E5E7E9"
MODEL_NAME = "house_price_model.joblib"
MODEL_PATH = base_dir / "pricing_model" / "house_price_model.joblib"