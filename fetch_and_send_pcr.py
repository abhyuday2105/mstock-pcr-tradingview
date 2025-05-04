import requests
import json

# Configuration
API_KEY = "your_api_key"
USER_ID = "your_user_id"
PASSWORD = "your_password"
TOTP = "your_totp"  # If applicable
BASE_URL = "https://api.mstock.com"
WEBHOOK_URL = "https://your-flask-app-url.com/update_pcr"

def login():
    payload = {
        "userId": USER_ID,
        "password": PASSWORD,
        "totp": TOTP,
        "apiKey": API_KEY
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    return response.json().get("data", {}).get("accessToken", "")

def fetch_option_chain(symbol, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/option-chain?symbol={symbol}", headers=headers)
    return response.json()

def calculate_pcr(data):
    calls = data.get("calls", [])
    puts = data.get("puts", [])
    call_oi = sum(item.get("openInterest", 0) for item in calls)
    put_oi = sum(item.get("openInterest", 0) for item in puts)
    return round(put_oi / call_oi, 2) if call_oi else 0

def send_pcr_to_web(symbol, pcr):
    payload = {"symbol": symbol, "pcr": pcr}
    requests.post(WEBHOOK_URL, json=payload)
    print(f"Sent {symbol} PCR: {pcr}")

def main():
    token = login()
    for symbol in ["NIFTY", "BANKNIFTY"]:
        data = fetch_option_chain(symbol, token)
        pcr = calculate_pcr(data)
        send_pcr_to_web(symbol, pcr)

if __name__ == "__main__":
    main()
