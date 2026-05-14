from flask import Flask, jsonify, request, send_file
from pathlib import Path

from template_engine import (
    list_templates,
    generate_template,
    validate_template,
    export_zip
)

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


@app.route("/templates/<template_name>/validate")
def validate(template_name):
    return jsonify(validate_template(template_name))


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

    except KeyError as e:
        return jsonify({
            "error": "Missing variables",
            "missing": list(e.args[0])
        }), 400

    except ValueError as e:
        return jsonify({
            "error": "Validation failed",
            "details": str(e)
        }), 400


@app.route("/export/<project_name>")
def export(project_name):
    try:
        zip_path = export_zip(project_name)
        return send_file(zip_path, as_attachment=True)

    except FileNotFoundError:
        return jsonify({
            "error": "Project not found"
        }), 404


if __name__ == "__main__":
    app.run(debug=True)
