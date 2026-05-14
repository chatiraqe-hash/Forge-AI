from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
ALLOWED_ROOTS = [
    BASE_DIR / "templates",
    BASE_DIR / "generated",
    BASE_DIR / "exports",
]


def resolve_safe_path(path: str) -> Path:
    candidate = (BASE_DIR / path).resolve()

    for root in ALLOWED_ROOTS:
        if candidate.is_relative_to(root.resolve()):
            return candidate

    raise PermissionError(f"Path is outside sandbox: {path}")