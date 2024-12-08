from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def format_diff(data_diff, format_name='stylish'):
    if format_name == 'stylish':
        return stylish(data_diff)
    elif format_name == 'plain':
        return plain(data_diff)
    elif format_name == 'json':
        return json_format(data_diff)
    raise ValueError("Unsupported format")
