from typing import Any

from template_registry.loader import list_templates


def search_templates(
    query: str = "",
    stack: str | None = None,
    category: str | None = None,
) -> list[dict[str, Any]]:
    templates = list_templates()
    results: list[dict[str, Any]] = []

    query_lower = query.lower().strip()

    for template in templates:
        if query_lower:
            searchable = " ".join(
                [
                    template.get("id", ""),
                    template.get("name", ""),
                    template.get("category", ""),
                    template.get("stack", ""),
                ]
            ).lower()

            if query_lower not in searchable:
                continue

        if stack and template.get("stack") != stack:
            continue

        if category and template.get("category") != category:
            continue

        results.append(template)

    return results