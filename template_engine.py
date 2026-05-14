from pathlib import Path
import json
import requests
import shutil
import zipfile

BASE_DIR = Path(__file__).parent

TEMPLATES_DIR = BASE_DIR / "templates"
GENERATED_DIR = BASE_DIR / "generated"
GITHUB_TEMPLATES_API = "https://api.github.com/repos/chatiraqe-hash/templates/contents"


def list_templates():
    if not TEMPLATES_DIR.exists():
        return []

    templates = []

    for item in TEMPLATES_DIR.iterdir():
        if item.is_dir() and (item / "template.json").exists():
            metadata = load_metadata(item.name)
            templates.append(metadata)

    return templates


def load_metadata(template_name):
    metadata_path = TEMPLATES_DIR / template_name / "template.json"

    if not metadata_path.exists():
        raise FileNotFoundError("Template metadata not found")

    return json.loads(metadata_path.read_text(encoding="utf-8-sig"))


def apply_variables(content, variables):
    for key, value in variables.items():
        placeholder = "{{" + key + "}}"
        content = content.replace(placeholder, str(value))

    return content


def validate_template(template_name):
    template_dir = TEMPLATES_DIR / template_name
    metadata_path = template_dir / "template.json"
    files_dir = template_dir / "files"

    errors = []

    if not template_dir.exists():
        errors.append("Template directory not found")

    if not metadata_path.exists():
        errors.append("template.json is missing")

    if not files_dir.exists():
        errors.append("files directory is missing")

    if errors:
        return {
            "valid": False,
            "errors": errors
        }

    metadata = load_metadata(template_name)

    required = [
        "name",
        "version",
        "stack",
        "category",
        "required_variables"
    ]

    for key in required:
        if key not in metadata:
            errors.append(f"metadata missing: {key}")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


def generate_template(template_name, output_name, variables=None):
    variables = variables or {}

    validation = validate_template(template_name)

    if not validation["valid"]:
        raise ValueError(validation["errors"])

    template_dir = TEMPLATES_DIR / template_name
    files_dir = template_dir / "files"

    metadata = load_metadata(template_name)

    required_variables = metadata.get("required_variables", [])

    missing_variables = [
        key for key in required_variables
        if key not in variables
    ]

    if missing_variables:
        raise KeyError(missing_variables)

    GENERATED_DIR.mkdir(exist_ok=True)

    output_dir = GENERATED_DIR / output_name

    if output_dir.exists():
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    for source_path in files_dir.rglob("*"):
        if source_path.is_dir():
            continue

        relative_path = source_path.relative_to(files_dir)
        target_path = output_dir / relative_path

        target_path.parent.mkdir(parents=True, exist_ok=True)

        content = source_path.read_text(encoding="utf-8-sig")
        final_content = apply_variables(content, variables)

        target_path.write_text(final_content, encoding="utf-8")

    return {
        "template": template_name,
        "output": str(output_dir),
        "metadata": metadata
    }


def export_zip(project_name):
    project_dir = GENERATED_DIR / project_name

    if not project_dir.exists():
        raise FileNotFoundError("Generated project not found")

    zip_path = GENERATED_DIR / f"{project_name}.zip"

    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in project_dir.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(project_dir)
                zipf.write(file_path, arcname)

    return str(zip_path)
