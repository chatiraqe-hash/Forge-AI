from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent / "templates"

def list_templates():
    if not TEMPLATES_DIR.exists():
        return []

    return [
        item.name
        for item in TEMPLATES_DIR.iterdir()
        if item.is_file()
    ]
