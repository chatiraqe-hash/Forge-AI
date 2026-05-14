import json
from typing import Any

from sandbox import resolve_safe_path
from template_registry.inheritance import resolve_inherited_manifest


def load_manifest(manifest_path: str) -> dict[str, Any]:
    path = resolve_safe_path(manifest_path)

    with path.open("r", encoding="utf-8") as file:
        manifest: dict[str, Any] = json.load(file)

    return resolve_inherited_manifest(manifest)