# mStock PCR to TradingView

This project fetches real-time Put/Call Ratio (PCR) data from the m.Stock API and serves it via a Flask webhook for integration with TradingView.

## Components

- `fetch_and_send_pcr.py`: Fetches PCR data and sends it to the Flask server.
- `app.py`: Flask application that stores and serves PCR data.
- `requirements.txt`: Python dependencies.

## Deployment

The Flask app can be deployed on platforms like Render for free hosting.

## Usage

1. Set your m.Stock API credentials in `fetch_and_send_pcr.py`.
2. Deploy the Flask app.
3. Run `fetch_and_send_pcr.py` periodically to update PCR data.
4. Use TradingView's Pine Script to fetch and display PCR data.
