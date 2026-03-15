from utils.load_prompt import load_prompt
from google import genai
from google.genai import types
from utils.config import CLIENT, MODEL, USER_COLOR, AGENT_COLOR, FUNCTION_COLOR

def research_agent(target_neighborhood: str) -> str:
    """
    Runs the real estate research agent.

    The agent analyzes the investment potential of a given neighborhood
    using a predefined system prompt and returns a structured report
    highlighting positive investment factors and living characteristics.

    Args:
        target_neighborhood (str): Name of the neighborhood to analyze.
        model: The model identifier to use (previously MODEL).

    Returns:
        str: Generated research report about the neighborhood.
    """
    
    system_prompt = load_prompt("research_agent_v1")
    response = CLIENT.models.generate_content(
        model = MODEL,
        contents=f"TARGET NEIGHBORHOOD {target_neighborhood}",
        config = types.GenerateContentConfig(
            system_instruction = system_prompt,
            tools=[types.Tool(google_search=types.GoogleSearch())],
            temperature=0.5
        ))
    
    return response.text