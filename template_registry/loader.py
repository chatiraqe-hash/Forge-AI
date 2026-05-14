import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
REGISTRY_PATH = BASE_DIR / "template_registry" / "registry.json"


def load_registry() -> dict[str, Any]:
    with REGISTRY_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def list_templates() -> list[dict[str, Any]]:
    registry = load_registry()
    return registry.get("templates", [])