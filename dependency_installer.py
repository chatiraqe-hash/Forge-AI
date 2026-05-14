from pathlib import Path
from typing import Any


def detect_install_command(manifest: dict[str, Any]) -> str:
    stack = manifest.get("stack")

    if stack == "python-flask":
        return "pip install -r requirements.txt"

    if stack == "node-express":
        return "npm install"

    if stack == "nextjs":
        return "npm install"

    return "manual install required"


def write_install_instructions(project_dir: str, manifest: dict[str, Any]) -> Path:
    path = Path(project_dir) / "INSTALL.md"
    command = detect_install_command(manifest)

    path.write_text(
        f"# Install Instructions\n\n```bash\n{command}\n```\n",
        encoding="utf-8",
    )

    return path