from template_registry.loader import list_templates


def main() -> None:
    templates = list_templates()

    print("\n=== Forge AI Template Registry ===\n")

    for template in templates:
        print(f"Name: {template['name']}")
        print(f"ID: {template['id']}")
        print(f"Version: {template['version']}")
        print(f"Stack: {template['stack']}")
        print("-" * 40)


if __name__ == "__main__":
    main()