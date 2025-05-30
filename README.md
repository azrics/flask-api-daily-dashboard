# Flask API Daily Dashboard 🚀

A lightweight Flask project to fetch and display real-time data from a public API (e.g., cryptocurrency prices, weather, or any RESTful service). Great for learning Flask, API integration, and dashboard UI basics.

---

## 🔧 Features

- Real-time data fetch using `requests`
- Simple dashboard with manual "Refresh" button
- Flask templates (Jinja2) for front-end rendering
- Optional: Save and view data history (last 7 fetches)
- Clean folder structure and modular design

---

## 📂 Folder Structure

flask-api-daily-dashboard/
├── app/
│ ├── templates/ → HTML frontend
│ ├── static/ → CSS/JS files
│ ├── routes.py → Flask routes
│ ├── api_handler.py → API call logic
│ └── init.py
├── config.py
├── history.json
├── run.py
└── requirements.txt


---

## 🚀 Quick Start

1. Clone the repo  
```bash
git clone https://github.com/yourusername/flask-api-daily-dashboard.git
cd flask-api-daily-dashboard
```

2. Create a Virtual Environment & activate it.
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run the app
```bash
python run.py
```

🌐 API Used
By default, this project uses the CoinGecko API for crypto prices. You can switch to any API by editing api_handler.py.

📦 Tech Stack
* Python 3.x

* Flask

* HTML/CSS/JS

* Requests (for API calls)

* JSON (for history storage)