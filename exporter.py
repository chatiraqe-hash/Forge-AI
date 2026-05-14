from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

from plugins.registry import run_plugins


def export_project(project_dir: str) -> Path:
    context = {
        "project_dir": Path(project_dir),
    }

    context = run_plugins("before_export", context)

    project_path = context["project_dir"]
    zip_path = project_path.with_suffix(".zip")

    with ZipFile(zip_path, "w", ZIP_DEFLATED) as zip_file:
        for file_path in project_path.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(project_path.parent)
                zip_file.write(file_path, arcname)

    context["zip_path"] = zip_path
    run_plugins("after_export", context)

    return zip_path