# Fetches data from a free API (e.g., OpenWeatherMap)  
import requests  
import sqlite3  
from datetime import datetime  

API_URL = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY"  

def fetch_data():  
    response = requests.get(API_URL)  
    data = response.json()  
    # Store in SQLite  
    conn = sqlite3.connect("data.db")  
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO weather VALUES (?, ?)", (datetime.now(), str(data)))  
    conn.commit()  
    conn.close()  

if __name__ == "__main__":  
    fetch_data()  