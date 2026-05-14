from exporter import export_project
from plugins.logger_plugin import log_export, log_generation
from plugins.registry import register_plugin
from template_engine_v2 import generate_project
from template_registry.loader import list_templates


register_plugin("before_generate", log_generation)
register_plugin("before_export", log_export)


def main() -> None:
    templates = list_templates()

    print("\n=== Forge AI Runtime ===\n")

    selected_template = templates[0]

    project = generate_project(
        selected_template["manifest_path"],
        {
            "PROJECT_NAME": "forge-runtime",
            "BOT_NAME": "forge_bot",
        },
    )

    archive = export_project(str(project))

    print("\nProject:")
    print(project)

    print("\nArchive:")
    print(archive)


if __name__ == "__main__":
    main()