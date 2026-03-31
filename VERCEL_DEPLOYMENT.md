# Vercel Deployment Guide for Car Price Prediction API

## Prerequisites
1. GitHub account with your project pushed
2. Vercel account (free at vercel.com)
3. All model files in repo: `linear_regression_ford.pkl`, `scaler.pkl`, `columns.pkl`

## Step 1: Push to GitHub
```bash
cd d:\Python\ML\CarPrice
git init
git add .
git commit -m "Car price prediction with FastAPI and HTML frontend"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CarPrice.git
git push -u origin main
```

## Step 2: Connect Vercel to GitHub
1. Go to vercel.com
2. Sign up / Log in
3. Click "New Project"
4. Select your GitHub repository "CarPrice"
5. Click "Import"

## Step 3: Configure Project Settings
On the Vercel import page, you should see:
- Framework Preset: "Other" (it auto-detects)
- Root Directory: `.` (leave as is)

Click "Continue" (no changes needed)

## Step 4: Add Environment Variables
Before deploying, add env vars:

In Vercel dashboard under your project > Settings > Environment Variables, add:

```
ALLOWED_ORIGINS = https://your-project-name.vercel.app
```

(Replace "your-project-name" with what Vercel assigned)

## Step 5: Deploy
Click "Deploy"

Wait 2-3 minutes for first build/deploy to complete.

## Step 6: Verify Deployment
Your app is now live at:
```
https://your-project-name.vercel.app
```

Test these URLs:
- Home: https://your-project-name.vercel.app/
- Health: https://your-project-name.vercel.app/health
- Docs: https://your-project-name.vercel.app/docs
- Categories: https://your-project-name.vercel.app/categories

## Step 7: Test Prediction (using Swagger UI)
1. Open: https://your-project-name.vercel.app/docs
2. Find "POST /predict"
3. Click "Try it out"
4. Fill in sample values:
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

Your should see predictions in both GBP and INR.

## Troubleshooting

### Cold start delay
First request takes 5-10 seconds (normal on serverless). Subsequent requests are fast.

### 404 on static files
Vercel serves `car_price_api/static/index.html` via FastAPI routes - this is handled automatically.

### Model files not found
Ensure these are in your repo root:
- linear_regression_ford.pkl
- scaler.pkl
- columns.pkl

### CORS errors
Check ALLOWED_ORIGINS env var matches your Vercel domain exactly.

## Future Updates
Any time you push to GitHub main, Vercel auto-redeploys.
```bash
git add .
git commit -m "Update message"
git push origin main
```

Vercel will auto-detect and re-deploy in 1-2 mins.
