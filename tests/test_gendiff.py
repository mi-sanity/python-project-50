import os

import pytest
from gendiff import generate_diff


def get_fixture_path(file_name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', file_name)


@pytest.mark.parametrize("file1, file2, formatter, file_result", [
    ("file1.json", "file2.json", "stylish", "result_stylish.txt"),
    ("file1.yml", "file2.yml", "stylish", "result_stylish.txt"),
    ("file1.json", "file2.json", "plain", "result_plain.txt"),
    ("file1.yml", "file2.yml", "plain", "result_plain.txt"),
    ("file1.json", "file2.json", "json", "result_json_format.txt"),
    ("file1.yml", "file2.yml", "json", "result_json_format.txt"),
])
def test_generate_diff(file1, file2, formatter, file_result):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    file_result_path = get_fixture_path(file_result)
    diff = generate_diff(file1_path, file2_path, formatter)
    expected_result = get_content(file_result_path)
    assert diff == expected_result


def get_content(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
