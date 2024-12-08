import json
import os

import yaml

FORMATTER_FUNCTIONS = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load
}


def get_content(file_name):
    file_content = open(file_name)
    return file_content


def parse_file(file_name, file_content):
    extension = os.path.splitext(file_name)[1].lower()
    if extension not in FORMATTER_FUNCTIONS:
        raise ValueError(f"Unsupported extension: {extension}")
    return FORMATTER_FUNCTIONS[extension](file_content)
