import json
from typing import Any

from sandbox import resolve_safe_path


def _load_parent_manifest(parent_path: str) -> dict[str, Any]:
    path = resolve_safe_path(parent_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def resolve_inherited_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    parent_path = manifest.get("extends")

    if not parent_path:
        return manifest

    parent = _load_parent_manifest(parent_path)

    resolved = {
        **parent,
        **manifest,
    }

    parent_variables = parent.get("variables", [])
    child_variables = manifest.get("variables", [])

    variable_map = {
        variable["name"]: variable
        for variable in parent_variables
    }

    for variable in child_variables:
        variable_map[variable["name"]] = variable

    resolved["variables"] = list(variable_map.values())

    return resolved