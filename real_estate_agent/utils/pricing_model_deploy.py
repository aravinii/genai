import joblib
import uvicorn
import socket
import threading

from fastapi import FastAPI
import pandas as pd

from pathlib import Path
import sys

repo_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(repo_root))

from real_estate_agent.utils.config import MODEL_PATH
from real_estate_agent.utils.transformers import zero_to_nan, clip_transformer

price_model = joblib.load(MODEL_PATH)

app = FastAPI(title="Property Pricing API")

@app.post("/predict")
def predict(input_data: dict) -> float:
        df = pd.DataFrame([input_data])
        return price_model.predict(df)[0]

def port_in_use(port: int, host: str = "0.0.0.0") -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            return False
        except OSError:
            return True

def start_server(host: str = "0.0.0.0", port: int = 8000):
    """
    Starts the FastAPI server in a background thread.

    This function is intended for use in environments like Jupyter notebooks,
    allowing the API to be launched without blocking the main thread. Once started, 
    the server will be available to serve requests (e.g., to agents that need to call the API).

    Args:
        host (str): The hostname to listen on. Defaults to "0.0.0.0".
        port (int): The port number to bind the server to. Defaults to 8000.

    Returns:
        threading.Thread: The thread running the API server in the background.
    """
    if port_in_use(port, host):
        return
    def _run():
        uvicorn.run(app, host=host, port=port, log_level="error")

    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
    return thread