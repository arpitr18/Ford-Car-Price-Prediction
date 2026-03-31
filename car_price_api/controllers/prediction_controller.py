from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

from car_price_api.models import CarInput, PredictionResponse
from car_price_api.services.prediction_service import PredictionService


router = APIRouter()
service = PredictionService()
BASE_DIR = Path(__file__).resolve().parent.parent
HOME_PAGE = BASE_DIR / "static" / "index.html"


@router.get("/")
def root() -> FileResponse:
    return FileResponse(HOME_PAGE)


@router.get("/api")
def api_info() -> dict[str, str]:
    return {"message": "Car Price Prediction API is running"}


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/categories")
def categories() -> dict[str, list[str]]:
    return service.category_options()


@router.post("/predict", response_model=PredictionResponse)
def predict_price(data: CarInput) -> dict:
    return service.predict(data)
