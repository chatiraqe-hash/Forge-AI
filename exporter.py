from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


def export_project(project_dir: str) -> Path:
    project_path = Path(project_dir)

    zip_path = project_path.with_suffix(".zip")

    with ZipFile(zip_path, "w", ZIP_DEFLATED) as zip_file:
        for file_path in project_path.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(project_path.parent)
                zip_file.write(file_path, arcname)

    return zip_path