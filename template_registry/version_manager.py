from typing import Any


def parse_version(version: str) -> tuple[int, int, int]:
    parts = version.split(".")

    if len(parts) != 3:
        raise ValueError(f"Invalid version format: {version}")

    return int(parts[0]), int(parts[1]), int(parts[2])


def is_newer_version(current: str, candidate: str) -> bool:
    return parse_version(candidate) > parse_version(current)


def find_upgrade(
    current_template: dict[str, Any],
    available_templates: list[dict[str, Any]],
) -> dict[str, Any] | None:
    current_id = current_template["id"]
    current_version = current_template["version"]

    candidates = [
        template
        for template in available_templates
        if template.get("id") == current_id
        and is_newer_version(current_version, template.get("version", "0.0.0"))
    ]

    if not candidates:
        return None

    return sorted(
        candidates,
        key=lambda template: parse_version(template["version"]),
        reverse=True,
    )[0]