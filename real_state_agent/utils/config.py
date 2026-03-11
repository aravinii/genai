import os
from google import genai
from dotenv import load_dotenv


load_dotenv()
CLIENT = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash"
USER_COLOR = "#D6EAF8"
AGENT_COLOR = "#F9E79F"
FUNCTION_COLOR = "#E5E7E9"