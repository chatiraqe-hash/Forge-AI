from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


@app.route("/")
def home():
    return jsonify({"status": "Forge AI running"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json(silent=True) or {}

    user_message = data.get("message", "")

    if not user_message:
        return jsonify({
            "ok": False,
            "error": "message is required"
        }), 400

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    response = requests.post(
        GROQ_URL,
        headers=headers,
        json=payload
    )

    result = response.json()

    if response.status_code != 200:
        return jsonify({
            "ok": False,
            "status_code": response.status_code,
            "groq_error": result
        }), response.status_code

    ai_reply = result["choices"][0]["message"]["content"]

    return jsonify({
        "ok": True,
        "input": user_message,
        "reply": ai_reply
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)