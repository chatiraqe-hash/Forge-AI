import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent


def load_manifest(manifest_path: str) -> dict[str, Any]:
    path = BASE_DIR / manifest_path

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)