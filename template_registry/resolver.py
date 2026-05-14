import json
from typing import Any

from sandbox import resolve_safe_path


def load_manifest(manifest_path: str) -> dict[str, Any]:
    path = resolve_safe_path(manifest_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)