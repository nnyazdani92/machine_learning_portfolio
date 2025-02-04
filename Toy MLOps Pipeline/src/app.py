import joblib

from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def load_model():
    global model
    model = joblib.load("models/model.pkl")

#TODO: Inference endpoint

@app.post("/predict")
def predict(features):
    pass