from utils.load_prompt import load_prompt
from utils.property import Property

from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json


def pricing_agent(model: str, info: dict) -> dict:
    """
    Runs the pricing agent.

    This agent is responsible for collecting all necessary information 
    about a property and its neighborhood and provide a price estimate.

    Always receives a structured JSON with (all keys must ALWAYS be present):

    {
        "info": {                       #'info': dictionary of fields that have been filled
            "bedrooms": int | null,
            "bathrooms": int | null,
            "area": float | null,
            "parking_slots": int | null,
            "neighborhood": str | null,
            "iptu": float | null
        },
        "comment": "...",               #'comment': short suggestion or status message for the next step
        "estimated_price": null         #'estimated_price': estimated_price for the property.
    }

    Args:
        model (str): Identifier of the model used for decision-making and pricing.
        info (dict): A dict containing pre-filled property attributes.

    Returns:
        dict: A JSON-like dictionary with the following structure:
            {
                "info": {
                    "bedrooms": int | null,
                    "bathrooms": int | null,
                    "area": float | null,
                    "parking_slots": int | null,
                    "neighborhood": str | null,
                    "iptu": float | null
                },
                "comment": "...",
                "estimated_price": float | null
            }
    """

    prompt = f"""
        DATA:

        {info}
    """
    
    CLIENT = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    response = CLIENT.models.generate_content(
        model = model,
        contents = prompt,
        config = types.GenerateContentConfig(
            system_instruction = load_prompt("pricing_agent_v1"),
            temperature = 0
        ))
    
    try:
        pricing_json = json.loads(response.text)
        
    except json.JSONDecodeError:
        pricing_json = {
            "info": info['property_info'],
            "comment": "Não foi possível gerar JSON. Tente novamente.",
            "estimated_price": None
        }
    
    return pricing_json