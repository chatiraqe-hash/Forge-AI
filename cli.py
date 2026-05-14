from exporter import export_project
from template_engine_v2 import generate_project
from template_registry.loader import list_templates


def main() -> None:
    templates = list_templates()

    print("\n=== Forge AI Template Registry ===\n")

    for index, template in enumerate(templates, start=1):
        print(f"{index}. {template['name']} ({template['version']})")

    selected_template = templates[0]

    project = generate_project(
        selected_template["manifest_path"],
        {
            "PROJECT_NAME": "forge-production",
            "BOT_NAME": "forge_bot",
        },
    )

    archive = export_project(str(project))

    print("\nProject Generated:")
    print(project)

    print("\nZIP Export:")
    print(archive)


if __name__ == "__main__":
    main()