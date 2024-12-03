import json
import yaml
import os


def parse_file(file_name):
    extension = os.path.splitext(file_name)[1].lower()
    parser = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }

    if extension not in parser:
        raise ValueError(f"Unsupported extension: {extension}")

    with open(file_name) as file:
        return parser[extension](file)
