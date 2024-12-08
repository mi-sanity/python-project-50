from gendiff.build_diff import build_diff
from gendiff.formatters.format_diff import format_diff
from gendiff.parser import get_content, parse_file


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_file(file1, get_content(file1))
    data2 = parse_file(file2, get_content(file2))
    data_diff = build_diff(data1, data2)
    diff = format_diff(data_diff, format_name)
    return diff
