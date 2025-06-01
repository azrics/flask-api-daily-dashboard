from flask import Flask, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Sample database setup
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            timestamp TEXT,
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Homepage - Dashboard UI
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# API Endpoint: Get latest weather data
@app.route('/api/weather')
def get_weather():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM weather ORDER BY timestamp DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    return jsonify({'timestamp': row[0], 'data': row[1]}) if row else jsonify({'error': 'No data'})

# API Endpoint: Manual data refresh
@app.route('/api/refresh')
def refresh_data():
    try:
        from scripts.data_fetcher import fetch_data
        fetch_data()
        return jsonify({'status': 'Data updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)