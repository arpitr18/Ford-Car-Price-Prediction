from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "linear_regression_ford.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"
COLUMNS_PATH = BASE_DIR / "columns.pkl"
DATA_PATH = BASE_DIR / "ford.csv"

GBP_TO_INR_RATE = 124.10

# Set ALLOWED_ORIGINS as comma-separated values in environment for production.
DEFAULT_ALLOWED_ORIGINS = [
    "https://heart-risk-prediction-by-heartlytics.vercel.app",
]


def get_allowed_origins() -> list[str]:
    raw_origins = os.getenv("ALLOWED_ORIGINS", "").strip()
    if not raw_origins:
        return DEFAULT_ALLOWED_ORIGINS

    origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]
    return origins or DEFAULT_ALLOWED_ORIGINS
