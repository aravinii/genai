import requests
from utils.config import DEFAULT_API_BASE


def predict_price(input_data: dict) -> float:
    """
    Get estimated property price from the model API (/predict).
    
    Args:
        input_data: Dictionary with property features:
            - bedrooms (int): number of bedrooms
            - bathrooms (int): number of bathrooms
            - parking_slots (int): number of parking spaces
            - area (int): area in m²
            - iptu (int): property tax value
            - neighborhood (str): neighborhood name
            - type (str): property type ('Apartamento' or 'Casa')
    
    Returns:
        Estimated price (float), rounded to 2 decimal places.
    
    Raises:
        requests.HTTPError: If the API returns 4xx/5xx.
        requests.RequestException: On network failure or timeout.
    """

    url = f"{DEFAULT_API_BASE.rstrip('/')}/predict"
    resp = requests.post(url, json=input_data, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return round(data, 2)