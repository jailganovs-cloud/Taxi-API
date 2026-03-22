from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TaxiInput(BaseModel):
    trip_distance: float
    passenger_count: int
    pickup_hour: int
    pickup_day: int

@app.get("/")
def home():
    return {"message": "Taxi Fare Prediction API is running"}

@app.post("/predict")
def predict(data: TaxiInput):
    score = data.trip_distance * 2 + data.passenger_count

    if score > 5:
        prediction = "high_fare"
        probability = 0.85
    else:
        prediction = "low_fare"
        probability = 0.90

    return {
        "prediction": prediction,
        "probability": probability
    }