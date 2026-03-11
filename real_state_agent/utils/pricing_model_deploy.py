from fastapi import FastAPI
import pickle
import os
from config import MODEL_PATH

with open(MODEL_PATH, "rb") as f:
    price_model = pickle.load(f)

app = FastAPI(title="Property Pricing API")

@app.post("/predict")
def predict():
    return {"message": "Hello, World!"}