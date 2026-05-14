from flask import Flask, jsonify
from pathlib import Path
from template_engine import list_templates

app = Flask(__name__)

TEMPLATES_DIR = Path(__file__).parent / "templates"

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

@app.route("/templates/<template_name>")
def get_template(template_name):
    template_path = TEMPLATES_DIR / template_name

    if not template_path.exists():
        return jsonify({
            "error": "Template not found"
        }), 404

    content = template_path.read_text(encoding="utf-8")

    return jsonify({
        "template": template_name,
        "content": content
    })

if __name__ == "__main__":
    app.run(debug=True)