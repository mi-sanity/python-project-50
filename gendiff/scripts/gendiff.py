from gendiff.data.build_diff import build_diff
from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.scripts.parser import get_extension, parse_file

FORMAT_NAMES = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format
}


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_file(file1, get_extension(file1))
    data2 = parse_file(file2, get_extension(file2))
    diff = build_diff(data1, data2)
    if isinstance(format_name, str):
        format_name = FORMAT_NAMES[format_name]
    diff = format_name(diff)
    return diff


def main():
    generate_diff()


if __name__ == '__main__':
    main()
