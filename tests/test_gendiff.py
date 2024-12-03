import pytest
from gendiff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, result", [
    ("tests/fixtures/file1.json", 
     "tests/fixtures/file2.json", 
     "stylish",
     "tests/fixtures/result_json_yml_yaml.txt"),
    ("tests/fixtures/file1.yml", 
     "tests/fixtures/file2.yml", 
     "stylish",
     "tests/fixtures/result_json_yml_yaml.txt"),
     ("tests/fixtures/file1.json", 
     "tests/fixtures/file2.json", 
     "plain",
     "tests/fixtures/result_plain.txt"),
    ("tests/fixtures/file1.yml", 
     "tests/fixtures/file2.yml", 
     "plain",
     "tests/fixtures/result_plain.txt"),
])


def test_generate_diff(file1, file2, formatter, result):
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(result)
    assert diff == expected_result


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
