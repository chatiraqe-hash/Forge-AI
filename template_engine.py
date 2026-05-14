from pathlib import Path
import shutil

BASE_DIR = Path(__file__).parent

TEMPLATES_DIR = BASE_DIR / "templates"
GENERATED_DIR = BASE_DIR / "generated"


def list_templates():
    if not TEMPLATES_DIR.exists():
        return []

    return [
        item.name
        for item in TEMPLATES_DIR.iterdir()
        if item.is_file()
    ]


def generate_template(template_name, output_name):
    template_path = TEMPLATES_DIR / template_name

    if not template_path.exists():
        raise FileNotFoundError("Template not found")

    GENERATED_DIR.mkdir(exist_ok=True)

    output_path = GENERATED_DIR / output_name

    shutil.copy(template_path, output_path)

    return {
        "template": template_name,
        "output": str(output_path)
    }