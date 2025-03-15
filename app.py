from flask import Flask, jsonify
import requests

app = Flask(__name__)


def fetch_nse_data():
    url = "https://www.nseindia.com/api/live-analysis-oi-spurts-underlyings"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/",
        "Accept-Encoding": "gzip, deflate, br",
    }

    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)  # Get session cookies
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data", "status": response.status_code}


@app.route("/nse_data", methods=["GET"])
def get_nse_data():
    return fetch_nse_data()


if __name__ == "__main__":
    app.run(debug=True)
