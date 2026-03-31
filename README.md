# 🚗 Car Price Prediction

A modern, full-stack AI-powered application to predict Ford car prices using Machine Learning. Built with FastAPI, scikit-learn, and a beautiful glass-morphism UI.

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135.2-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0+-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

---

## ✨ Features

- 🤖 **Linear Regression Model** — Trained on Ford UK car dataset with high accuracy
- 💷 **Dual Currency Support** — Prices in GBP and INR (auto-converted at 124.10 rate)
- 🎨 **Glass-morphism UI** — Beautiful, modern frontend with animated car graphics
- ⚡ **REST API** — FastAPI with auto-generated Swagger documentation
- 🌐 **Serverless Ready** — Vercel deployment-compatible
- 📊 **Category Validation** — Detailed error responses with allowed values
- 🔒 **CORS Protection** — Environment-configurable allowed origins

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/CarPrice.git
   cd CarPrice
   ```

2. **Create virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   
   Server will start at: `http://127.0.0.1:8000`

5. **Open in browser**
   - Homepage: http://127.0.0.1:8000/
   - API Docs: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

---

## 📋 API Endpoints

### `GET /` 
Returns the homepage HTML with the prediction form.
```bash
curl http://127.0.0.1:8000/
```

### `GET /health`
Health check endpoint for monitoring.
```bash
curl http://127.0.0.1:8000/health
# Response: {"status": "healthy"}
```

### `GET /categories`
Returns all allowed values for categorical fields.
```bash
curl http://127.0.0.1:8000/categories
# Response: {
#   "transmission": ["Manual", "Automatic"],
#   "fuelType": ["Diesel", "Petrol", "Hybrid", "Other"],
#   "model": ["Fiesta", "Focus", "Kuga", ...]
# }
```

### `POST /predict`
Make a car price prediction.

**Request Body:**
```json
{
  "model": "Fiesta",
  "year": 2017,
  "transmission": "Manual",
  "mileage": 15735,
  "fuelType": "Petrol",
  "tax": 150,
  "mpg": 57.7,
  "engineSize": 1.0
}
```

**Response (Success):**
```json
{
  "predicted_price_gbp": 11032.53,
  "predicted_price_inr": 1369137.17,
  "exchange_rate": 124.10
}
```

**Response (Validation Error):**
```json
{
  "error": "Invalid input provided",
  "fields": {
    "fuelType": {
      "value": "Electric",
      "allowed_values": ["Diesel", "Petrol", "Hybrid", "Other"]
    }
  }
}
```

---

## 📁 Project Structure

```
CarPrice/
├── app.py                          # Local development entry point
├── requirements.txt                # Python dependencies
├── vercel.json                     # Vercel serverless config
├── .gitignore                      # Git ignore rules
├── ford.csv                        # Training dataset (git-ignored)
├── data.ipynb                      # Jupyter notebook (git-ignored)
│
├── api/
│   └── index.py                    # Vercel serverless handler
│
└── car_price_api/
    ├── main.py                     # FastAPI app setup & routing
    ├── config.py                   # Configuration & paths
    ├── models.py                   # Pydantic request/response schemas
    │
    ├── services/
    │   └── prediction_service.py   # ML inference logic
    │
    ├── controllers/
    │   └── prediction_controller.py # HTTP route handlers
    │
    ├── static/
    │   └── index.html              # Frontend UI (glass-morphism)
    │
    └── models/
        ├── linear_regression_ford.pkl
        ├── scaler.pkl
        └── columns.pkl
```

---

## 🏗️ Architecture

### MVC Design Pattern
```
Controller (HTTP Routes)
    ↓
Service (Business Logic & ML)
    ↓
Model Layer (Pydantic Schemas)
```

### ML Model Pipeline
```
Raw Input → Encoding (LabelEncoder)
          → Scaling (StandardScaler)
          → Prediction (Linear Regression)
          → GBP/INR Conversion
```

### Tech Stack

| Layer | Technology |
|-------|-----------|
| **API Framework** | FastAPI 0.135.2 |
| **ML** | scikit-learn 1.3.0, pandas 2.0+ |
| **Serialization** | joblib 1.3.0 |
| **Frontend** | HTML5, CSS3 (Glass-morphism) |
| **Deployment** | Vercel (Serverless) |

---

## 🌐 Deployment

### Deploy to Vercel (Production)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Car price prediction app"
   git push origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project" → Select your repo → Click "Import"

3. **Add Environment Variables** (in Vercel Dashboard)
   ```
   ALLOWED_ORIGINS = https://your-project-name.vercel.app
   ```

4. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app is live! 🎉

**Live at:** `https://your-project-name.vercel.app`

---

## 🧪 Testing

### Using Swagger UI
1. Navigate to `http://127.0.0.1:8000/docs` (local) or Vercel deployment `/docs`
2. Click on `POST /predict`
3. Click "Try it out"
4. Fill in test data:
   ```json
   {
     "model": "Fiesta",
     "year": 2017,
     "transmission": "Manual",
     "mileage": 15735,
     "fuelType": "Petrol",
     "tax": 150,
     "mpg": 57.7,
     "engineSize": 1.0
   }
   ```
5. Click "Execute"

### Using cURL
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Fiesta",
    "year": 2017,
    "transmission": "Manual",
    "mileage": 15735,
    "fuelType": "Petrol",
    "tax": 150,
    "mpg": 57.7,
    "engineSize": 1.0
  }'
```

---

## 🎨 UI Features

- **Glass-morphism Effect** — Translucent cards with backdrop blur
- **Animated Cars** — SVG cars driving across the screen
- **Responsive Design** — Works on desktop, tablet, mobile
- **Real-time Validation** — Shows allowed categories on page load
- **Live Results** — Displays predicted prices in GBP & INR
- **Professional Branding** — Space Grotesk font, smooth gradients

---

## 🔧 Configuration

### Environment Variables

Create `.env` file in project root (for local development):

```env
ALLOWED_ORIGINS=http://localhost:8000,http://localhost:3000
GBP_TO_INR_RATE=124.10
```

For Vercel, add these in Dashboard → Settings → Environment Variables.

### Allowed Car Models
Currently trained on these Ford models:
- Fiesta
- Focus
- Kuga
- B-Max
- Galaxy
- Mondeo
- S-Max
- Titanium
- Ecosport

---

## 📊 Model Performance

- **Algorithm:** Linear Regression
- **Training Data:** Ford UK car dataset
- **Features:** 8 input features (model, year, transmission, mileage, fuel type, tax, MPG, engine size)
- **Output:** Predicted price in GBP

---

## 🚦 Error Handling

All errors return detailed JSON responses:

```json
{
  "error": "Invalid input provided",
  "fields": {
    "transmission": {
      "value": "CVT",
      "allowed_values": ["Manual", "Automatic"]
    },
    "fuelType": {
      "value": "LPG",
      "allowed_values": ["Diesel", "Petrol", "Hybrid", "Other"]
    }
  }
}
```

---

## 🔐 Security

- ✅ CORS whitelist enforcement
- ✅ Input validation on all endpoints
- ✅ Environment-based configuration
- ✅ No sensitive data in repository
- ✅ Models/CSVs in `.gitignore`

---

## 📈 Future Enhancements

- [ ] Multiple regression models (Random Forest, XGBoost)
- [ ] Model performance metrics dashboard
- [ ] Price history trends
- [ ] Real-time market data integration
- [ ] User accounts & saved predictions
- [ ] Mobile app (React Native)
- [ ] Database for storing predictions

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 💬 Support

For issues or questions, please open an [GitHub Issue](https://github.com/YOUR_USERNAME/CarPrice/issues).

---

## 📞 Contact

- **Author:** Your Name
- **Email:** your.email@example.com
- **GitHub:** [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

<div align="center">

**Made with ❤️ and ML**

⭐ If you found this helpful, please give it a star!

</div>
