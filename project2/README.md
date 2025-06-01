## 1. Clone & Install
* git clone https://github.com/your-repo/flask-api-daily-dashboard.git  
* cd flask-api-daily-dashboard  
* pip install -r requirements.txt  

## 2. Set Up API Keys
### 🌦️ Weather Data (OpenWeatherMap)
* Sign up at OpenWeatherMap.
* Get a free API key.
* Replace in scripts/data_fetcher.py:
  API_URL = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY"  # ← Paste key here  

## 🛠️ How to Use
### Run the Flask App

python app.py  # Visithttp://localhost:5000  


## CI/CD Pipeline
### GitHub Actions auto-runs on git push.

### Edit .github/workflows/python-ci.yml to deploy to Render/Heroku.