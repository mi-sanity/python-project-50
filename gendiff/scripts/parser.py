import json
import os


def parse_file(file_path):
    view = os.path.splitext(file_path)[1].lower()
    parser = {
        '.json': json.load,
    }

    if view not in parser:
        raise ValueError(f"Unsupported file format: {view}")

    with open(file_path) as file:
        return parser[view](file)
