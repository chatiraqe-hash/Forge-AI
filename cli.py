from template_registry.loader import list_templates
from template_registry.resolver import load_manifest


def main() -> None:
    templates = list_templates()

    print("\n=== Forge AI Registry Validation ===\n")

    for template in templates:
        manifest = load_manifest(template["manifest_path"])

        print(f"Template: {manifest['name']}")
        print(f"Stack: {manifest['stack']}")
        print(f"Entrypoint: {manifest['entrypoint']}")
        print("-" * 40)


if __name__ == "__main__":
    main()