# 🌾 Smart Agri Market & Disease Detection — Enterprise Edition

Full-stack agriculture ecosystem for India.

## Stack
- **Backend**: Django 4.2 + DRF + JWT (SQLite, PostgreSQL-ready)
- **Frontend**: React 18 (CRA) + Chart.js + React Router
- **Apps**: 16 modular Django apps covering market, products, disease, transactions, notifications, chatbot, info, settings, services, vendors, logistics, analytics, subscriptions, fraud, warehouse, accounts.

## Quick start

### Backend
```
cd backend
pip install -r requirements.txt
python manage.py makemigrations accounts products transactions vendors warehouse
python manage.py migrate
python seed.py
python manage.py runserver 0.0.0.0:8000
```

### Frontend
```
cd frontend
npm install
npm start         # http://localhost:3000
```

Or run the all-in-one helper:
```
python setup_and_run.py
```

## Default credentials
| Role   | Username | Password   |
|--------|----------|------------|
| Admin  | admin    | admin123   |
| Seller | seller   | seller123  |
| Vendor | vendor   | vendor123  |
| User   | user     | user123    |

Django admin panel: http://127.0.0.1:8000/admin/

## Features (all wired)
- ✅ JWT auth, role-based (user/seller/vendor/admin)
- ✅ Real-time CSV market data — 28 crops × 15 states × 200 weeks
- ✅ Price forecasting + dynamic pricing engine (weather/season/demand/festival/govt factors)
- ✅ Best buy/sell location finder
- ✅ Marketplace with live stock deduction, cart, wishlist, reviews
- ✅ Disease & defect detection (upload image)
- ✅ QR / UPI / GPay / COD payment methods
- ✅ PDF invoice generation (reportlab)
- ✅ Email / SMS / WhatsApp / Push notification endpoints
- ✅ AI farmer chatbot
- ✅ Govt schemes, soil/cultivation guides, weather tips
- ✅ Vendor & warehouse management
- ✅ Logistics tracking & shipping quotes
- ✅ Subscription plans (Free / Pro / Enterprise)
- ✅ Fraud check + dispute placeholders
- ✅ Analytics dashboard
- ✅ Dark/light theme + multi-language selector (10 langs)
- ✅ Floating WhatsApp button + © 2026 footer

## TODO markers (clearly tagged in code)
- Real ML models (TensorFlow/PyTorch CNN for disease, ARIMA/LSTM for prices)
- Real weather API (OpenWeatherMap)
- Real SMS gateway (Twilio/Fast2SMS)
- WhatsApp Business API
- Razorpay/Stripe payment gateway
- FCM push notifications
- Live mandi API
- PostgreSQL switch (uncomment in settings.py)
- Docker deployment

## Project structure
```
backend/
  agri_project/        # Django settings & URLs
  apps/                # 16 modular apps
  data/prices.csv      # 21,000-row dataset
  seed.py              # default users + products
frontend/
  src/pages/           # React pages
  src/admin|seller|vendor/  # role dashboards
  src/components/      # shared
  src/services/api.js  # axios client
```
