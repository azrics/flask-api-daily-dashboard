# app/api_handler.py
import requests

def fetch_crypto_data():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin,ethereum,dogecoin",
            "vs_currencies": "usd"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "Bitcoin (BTC)": f"${data['bitcoin']['usd']}",
            "Ethereum (ETH)": f"${data['ethereum']['usd']}",
            "Dogecoin (DOGE)": f"${data['dogecoin']['usd']}"
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching crypto data: {e}")
        return {
            "Bitcoin (BTC)": "N/A",
            "Ethereum (ETH)": "N/A",
            "Dogecoin (DOGE)": "N/A"
        }