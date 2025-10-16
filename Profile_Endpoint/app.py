#!/usr/bin/env python3
from flask import Flask, jsonify
from datetime import datetime, timezone
# import requests

app = Flask(__name__)

@app.route('/me', methods=['GET'], strict_slashes=False)
def my_profile():
    try:
        facts = requests.get('https://catfact.ninja/fact', timeout=10)
        facts.raise_for_status()
        fact = facts.json().get('fact')
    except Exception as e:
        print(f"Error fetching cat fact: {e}")
        fact = "Unable to fetch cat fact at this time"

    profile = {
        "status": "success",
        "user": {
            "email": "ajumobiabdulquyum@gmail.com",
            "name": "Ajumobi Abdulquyum",
            "stack": ["Python", "Flask", "PHP", "Laravel"]
        },
        "timestamp": str(datetime.now(timezone.utc)),
        "fact": fact
    }

    return jsonify(profile)

if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0", debug=True)