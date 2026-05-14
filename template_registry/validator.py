from typing import Any


REQUIRED_FIELDS = [
    "id",
    "name",
    "version",
    "category",
    "stack",
    "description",
    "author",
    "entrypoint",
    "variables",
]

SUPPORTED_VARIABLE_TYPES = {"string", "number", "boolean"}


def validate_manifest(manifest: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in manifest:
            errors.append(f"Missing required field: {field}")

    variables = manifest.get("variables", [])
    if not isinstance(variables, list):
        errors.append("variables must be a list")
        return False, errors

    for index, variable in enumerate(variables):
        if not isinstance(variable, dict):
            errors.append(f"variables[{index}] must be an object")
            continue

        if "name" not in variable:
            errors.append(f"variables[{index}] missing name")

        if "type" not in variable:
            errors.append(f"variables[{index}] missing type")
        elif variable["type"] not in SUPPORTED_VARIABLE_TYPES:
            errors.append(
                f"variables[{index}] has unsupported type: {variable['type']}"
            )

        if "required" not in variable:
            errors.append(f"variables[{index}] missing required")

    return len(errors) == 0, errors