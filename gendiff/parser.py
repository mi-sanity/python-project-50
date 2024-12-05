import json
import os
import yaml

FORMAT_FILES = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load
}


def get_extension(file):
    extension = os.path.splitext(file)[1].lower()
    return extension


def parse_file(file_name, extension):
    if extension not in FORMAT_FILES:
        raise ValueError(f"Unsupported extension: {extension}")

    with open(file_name) as file:
        return FORMAT_FILES[extension](file)
