#!/bin/env python3
from flask import Flask, jsonify
from datetime import datetime, timezone
import requests

app = Flask(__name__)

facts = requests.get('https://catfact.ninja/fact')
fact = facts.json().get('fact')

@app.route('/me', methods=['GET'], strict_slashes=False)
def my_profile():
    return jsonify({
        "status": "success",
        "user": {
            "email": "ajumobiabdulquyum@gmail.com",
            "name": "Ajumobi Abdulquyum",
            "stack": ["Python", "Flask", "PHP", "Laravel"]
        },
        "timestamp": str(datetime.now(timezone.utc)),
        "fact": fact
    })


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
