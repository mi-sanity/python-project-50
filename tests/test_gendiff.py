import pytest
from gendiff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, result", [
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'json',
     "tests/fixtures/result_json.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", 'yml',
     "tests/fixtures/result_yml.txt"),
])


def test_generate_diff(file1, file2, formatter, result):
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(result)
    assert diff == expected_result


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()