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

@app.route("/templates/<path:template_name>")
def get_template(template_name):
    template_path = (TEMPLATES_DIR / template_name).resolve()
    templates_root = TEMPLATES_DIR.resolve()

    if not str(template_path).startswith(str(templates_root)):
        return jsonify({
            "error": "Invalid template path"
        }), 400

    if not template_path.exists() or not template_path.is_file():
        return jsonify({
            "error": "Template not found"
        }), 404

    content = template_path.read_text(encoding="utf-8-sig")

    return jsonify({
        "template": template_name,
        "content": content
    })

if __name__ == "__main__":
    app.run(debug=True)