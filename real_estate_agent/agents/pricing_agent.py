from google import genai
from google.genai import types
import json

from utils.config import CLIENT, MODEL, USER_COLOR, AGENT_COLOR, FUNCTION_COLOR
from utils.load_prompt import load_prompt
from utils.pricing import predict_price
from utils.property import Property



def pricing_agent(info: dict) -> dict:
    """
    Runs the pricing agent.

    This agent is responsible for collecting all necessary information 
    about a property and its neighborhood and provide a price estimate.

    Always receives a structured JSON with (all keys must ALWAYS be present):

    {
        "info": {                       #'info': dictionary of fields that have been filled
            "bedrooms": int | null,
            "bathrooms": int | null,
            "parking_slots": int | null,
            "area": int | null,
            "iptu": int | null,
            "neighborhood": str | null,
            "type": str | null
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
                    "info": {                       #'info': dictionary of fields that have been filled
                        "bedrooms": int | null,
                        "bathrooms": int | null,
                        "parking_slots": int | null,
                        "area": int | null,
                        "iptu": int | null,
                        "neighborhood": str | null,
                        "type": str | null
                },
                    "comment": "...",
                    "estimated_price": float | null
                }
    """

    prompt = f"""
        DATA:

        {info}
    """

    response = CLIENT.models.generate_content(
        model = MODEL,
        contents = prompt,
        config = types.GenerateContentConfig(
            system_instruction = load_prompt("pricing_agent_v2"),
            response_mime_type="application/json",
            temperature = 0
        ))

    try:
        pricing_json = json.loads(response.text)
        inf = pricing_json.get("info", {})
        prop = Property.from_dict(inf)
        if prop.is_complete():
            try:
                pricing_json["estimated_price"] = predict_price(inf)
                pricing_json["comment"] = "Preço estimado com sucesso."
            except Exception:
                pricing_json["estimated_price"] = None
                pricing_json["comment"] = "API de preço indisponível."
        
    except json.JSONDecodeError:
        pricing_json = {
            "info": info['property_info'],
            "comment": "Não foi possível gerar JSON. Tente novamente.",
            "estimated_price": None
        }
    
    return pricing_json