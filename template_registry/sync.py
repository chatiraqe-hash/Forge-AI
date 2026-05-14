from typing import Any

from template_registry.loader import load_registry
from template_registry.remote import fetch_remote_registry


def sync_registries() -> dict[str, Any]:
    local_registry = load_registry()
    remote_registry = fetch_remote_registry()

    return {
        "local_templates": len(local_registry.get("templates", [])),
        "remote_templates": len(remote_registry.get("templates", [])),
        "sync_status": "ok",
    }