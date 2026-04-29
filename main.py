# CS 335 — Introduction to Artificial Intelligence
# API Assignment Starter Code — Northeastern Illinois University

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MY_API_KEY")

if not API_KEY:
    print("WARNING: No API key found (not needed for Open-Meteo)")

BASE_URL = "https://api.open-meteo.com/v1/forecast"

HEADERS = {
    "Content-Type": "application/json"
}


def divider(label):
    print(f"\n{'=' * 50}\n{label}\n{'=' * 50}")


# ── Call 1: GET request ───────────────────────────────────
def call_one_get():
    divider("CALL 1 — Chicago Weather")

    url = BASE_URL
    params = {
        "latitude": 41.88,
        "longitude": -87.63,
        "current_weather": True
    }

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        print(json.dumps(response.json()["current_weather"], indent=2))
    else:
        print(f"[ERROR] {response.status_code}")


# ── Call 2: POST request ─────────────
def call_two_post():
    divider("CALL 2 — New York Weather")

    url = BASE_URL
    payload = {
        "latitude": 40.71,
        "longitude": -74.00,
        "current_weather": True
    }

    response = requests.get(url, headers=HEADERS, params=payload)

    if response.status_code == 200:
        print(json.dumps(response.json()["current_weather"], indent=2))
    else:
        print(f"[ERROR] {response.status_code}")


# ── Call 3: Parameterized POST ────────────────────────────
def call_three_parameterized(user_input: str):
    divider(f"CALL 3 — Parameterized ({user_input})")

    url = BASE_URL

    if user_input.lower() == "chicago":
        lat, lon = 41.88, -87.63
    else:
        lat, lon = 40.71, -74.00

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        print(json.dumps(response.json()["current_weather"], indent=2))
    else:
        print(f"[ERROR] {response.status_code}")


if __name__ == "__main__":
    call_one_get()
    call_two_post()
    call_three_parameterized("Miami weather loaded successfully")
