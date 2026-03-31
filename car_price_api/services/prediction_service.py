from typing import Any

import joblib
import pandas as pd
from fastapi import HTTPException
from sklearn.preprocessing import LabelEncoder

from car_price_api.config import COLUMNS_PATH, DATA_PATH, GBP_TO_INR_RATE, MODEL_PATH, SCALER_PATH
from car_price_api.models import CarInput


class PredictionService:
    def __init__(self) -> None:
        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)
        self.expected_columns = joblib.load(COLUMNS_PATH)
        self.encoders = self._build_encoders()

    def _build_encoders(self) -> dict[str, LabelEncoder]:
        df = pd.read_csv(DATA_PATH)
        encoders: dict[str, LabelEncoder] = {}
        for col in ["model", "transmission", "fuelType"]:
            le = LabelEncoder()
            le.fit(df[col].astype(str).str.strip())
            encoders[col] = le
        return encoders

    def _get_allowed_values(self, column_name: str) -> list[str]:
        return self.encoders[column_name].classes_.tolist()

    def _encode_or_collect_error(self, column_name: str, raw_value: str, errors: list[dict[str, Any]]) -> int | None:
        encoder = self.encoders[column_name]
        normalized = str(raw_value).strip()
        if normalized not in encoder.classes_:
            errors.append(
                {
                    "field": column_name,
                    "invalid_value": raw_value,
                    "allowed_values": self._get_allowed_values(column_name),
                }
            )
            return None
        return int(encoder.transform([normalized])[0])

    def predict(self, data: CarInput) -> dict[str, Any]:
        errors: list[dict[str, Any]] = []

        model_encoded = self._encode_or_collect_error("model", data.model, errors)
        transmission_encoded = self._encode_or_collect_error("transmission", data.transmission, errors)
        fuel_type_encoded = self._encode_or_collect_error("fuelType", data.fuelType, errors)

        if errors:
            raise HTTPException(
                status_code=400,
                detail={
                    "message": "One or more categorical fields have invalid values.",
                    "errors": errors,
                },
            )

        row = {
            "model": model_encoded,
            "year": data.year,
            "transmission": transmission_encoded,
            "mileage": data.mileage,
            "fuelType": fuel_type_encoded,
            "tax": data.tax,
            "mpg": data.mpg,
            "engineSize": data.engineSize,
        }

        input_df = pd.DataFrame([row])
        input_df = input_df[self.expected_columns]

        scaled_array = self.scaler.transform(input_df)
        scaled_input = pd.DataFrame(scaled_array, columns=self.expected_columns)

        price_gbp = float(self.model.predict(scaled_input)[0])
        price_inr = price_gbp * GBP_TO_INR_RATE

        return {
            "predicted_price_gbp": round(price_gbp, 2),
            "predicted_price_inr": round(price_inr, 2),
            "exchange_rate_used": GBP_TO_INR_RATE,
            "base_currency": "GBP",
            "target_currency": "INR",
        }

    def category_options(self) -> dict[str, list[str]]:
        return {
            "model": self._get_allowed_values("model"),
            "transmission": self._get_allowed_values("transmission"),
            "fuelType": self._get_allowed_values("fuelType"),
        }
