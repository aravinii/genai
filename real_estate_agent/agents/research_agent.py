from utils.load_prompt import load_prompt
from google.genai import types
from utils.config import CLIENT, MODEL

def research_agent(target_neighborhood: str) -> str:
    f"""
    Runs the real estate research agent.

    The agent analyzes the investment potential of a given neighborhood
    using a predefined system prompt and returns a structured report
    highlighting positive investment factors and living characteristics.

    Args:
        target_neighborhood (str): Name of the neighborhood to analyze.

    Returns:
        dict: A dictionary containing:
            - "result" (str): The generated research report about the analyzed neighborhood.
            - "metadata" (dict): The metadata returned by the model response.
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

    total_tokens = getattr(response.usage_metadata, "total_token_count", None)
    if total_tokens and total_tokens > 0:
        return {"result": response.text, "metadata": total_tokens}
    else:
        return {"result": response.text, "metadata": None}
    
    