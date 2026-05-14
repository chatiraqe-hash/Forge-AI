from flask import Flask, request, jsonify

app = Flask(__name__)

BOT_NAME = "{{BOT_NAME}}"

@app.route("/")
def home():
    return jsonify({
        "bot": BOT_NAME,
        "status": "running"
    })

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json() or {}

    return jsonify({
        "bot": BOT_NAME,
        "received": data
    })

if __name__ == "__main__":
    app.run(debug=True)
