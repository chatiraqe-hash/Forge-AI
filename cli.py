from exporter import export_project
from plugins.logger_plugin import log_export, log_generation
from plugins.registry import register_plugin
from template_engine_v2 import generate_project
from template_registry.search import search_templates
from template_registry.version_manager import find_upgrade


register_plugin("before_generate", log_generation)
register_plugin("before_export", log_export)


def main() -> None:
    print("\n=== Forge AI Marketplace ===\n")

    templates = search_templates()

    for index, template in enumerate(templates, start=1):
        print(
            f"{index}. "
            f"{template['name']} | "
            f"{template['stack']} | "
            f"{template['category']} | "
            f"v{template['version']}"
        )

    upgrade = find_upgrade(
        {"id": "telegram-bot", "version": "1.0.0"},
        templates,
    )

    print("\nUpgrade Check:")
    print(upgrade)

    selected_template = templates[0]

    project = generate_project(
        selected_template["manifest_path"],
        {
            "PROJECT_NAME": "forge-versioned",
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