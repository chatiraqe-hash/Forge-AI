from flask import Flask, jsonify
from template_engine import list_templates

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Forge AI",
        "phase": "Phase 3"
    })

@app.route("/templates")
def templates():
    return jsonify({
        "templates": list_templates()
    })

if __name__ == "__main__":
    app.run(debug=True)
