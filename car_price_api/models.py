from pydantic import BaseModel, Field


class CarInput(BaseModel):
    model: str = Field(..., description="Ford model name, e.g., Fiesta")
    year: int = Field(..., ge=1990, le=2035)
    transmission: str = Field(..., description="Transmission type")
    mileage: int = Field(..., ge=0)
    fuelType: str = Field(..., description="Fuel type")
    tax: int = Field(..., ge=0)
    mpg: float = Field(..., gt=0)
    engineSize: float = Field(..., gt=0)


class PredictionResponse(BaseModel):
    predicted_price_gbp: float
    predicted_price_inr: float
    exchange_rate_used: float
    base_currency: str
    target_currency: str
