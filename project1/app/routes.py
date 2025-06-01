# app/routes.py
from flask import Blueprint, render_template, request
from datetime import datetime
from .api_handler import fetch_crypto_data

main = Blueprint('main', __name__)
history_log = []

@main.route("/", methods=["GET", "POST"])
def index():
    data = fetch_crypto_data()
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
                           source_name="CoinGecko API")