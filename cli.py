import argparse

from template_engine import (
    generate_template,
    export_zip
)

parser = argparse.ArgumentParser()

parser.add_argument("--template", required=True)
parser.add_argument("--output", required=True)
parser.add_argument("--project")
parser.add_argument("--bot")

args = parser.parse_args()

variables = {
    "PROJECT_NAME": args.project or "Forge AI Project",
    "BOT_NAME": args.bot or "ForgeBot"
}

result = generate_template(
    args.template,
    args.output,
    variables
)

zip_path = export_zip(args.output)

print(result)
print({
    "zip": zip_path
})
