# app/routes.py
from flask import Blueprint, render_template, request
from datetime import datetime
import random

main = Blueprint('main', __name__)

# Mock history (you can switch to file or DB later)
history_log = []

def mock_api_fetch():
    """Simulates API data response"""
    return {
        "Bitcoin (BTC)": f"${random.randint(25000, 31000)}",
        "Ethereum (ETH)": f"${random.randint(1500, 2500)}",
        "Dogecoin (DOGE)": f"${random.uniform(0.05, 0.15):.3f}"
    }

@main.route("/", methods=["GET", "POST"])
def index():
    data = mock_api_fetch()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add to history
    history_log.insert(0, {
        "timestamp": timestamp,
        "summary": f"BTC: {data['Bitcoin (BTC)']}, ETH: {data['Ethereum (ETH)']}"
    })
    history = history_log[:5]

    return render_template("index.html", 
                           data=data, 
                           timestamp=timestamp, 
                           history=history, 
                           source_name="Mock Crypto API")