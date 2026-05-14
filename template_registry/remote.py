from typing import Any


REMOTE_REGISTRY_URL = "https://example.com/forge-ai/registry.json"


def fetch_remote_registry() -> dict[str, Any]:
    return {
        "remote_url": REMOTE_REGISTRY_URL,
        "templates": [],
        "status": "placeholder",
    }