from flask import Flask, jsonify, request
from pathlib import Path
from template_engine import list_templates, generate_template

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
        return jsonify({"error": "Invalid template path"}), 400

    if not template_path.exists() or not template_path.is_file():
        return jsonify({"error": "Template not found"}), 404

    content = template_path.read_text(encoding="utf-8-sig")

    return jsonify({
        "template": template_name,
        "content": content
    })

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json() or {}

    template_name = data.get("template")
    output_name = data.get("output")
    variables = data.get("variables", {})

    if not template_name or not output_name:
        return jsonify({
            "error": "template and output are required"
        }), 400

    try:
        result = generate_template(
            template_name,
            output_name,
            variables
        )

        return jsonify(result)

    except FileNotFoundError:
        return jsonify({
            "error": "Template not found"
        }), 404

if __name__ == "__main__":
    app.run(debug=True)
