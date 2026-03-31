from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from car_price_api.config import get_allowed_origins
from car_price_api.controllers.prediction_controller import router


app = FastAPI(title="Car Price Prediction API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router)
