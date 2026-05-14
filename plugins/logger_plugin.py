from typing import Any


def log_generation(context: dict[str, Any]) -> dict[str, Any]:
    manifest = context["manifest"]

    print(f"[PLUGIN] Generating: {manifest['name']}")

    return context


def log_export(context: dict[str, Any]) -> dict[str, Any]:
    project_dir = context["project_dir"]

    print(f"[PLUGIN] Exporting: {project_dir}")

    return context