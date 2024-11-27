import argparse
# from gendiff.scripts.creat_diff import creat_diff
# from gendiff.scripts.parser import parse_file
import json
from gendiff.scripts.build_diff import build_diff


def generate_diff(file_path1, file_path2):
    # data1 = parse_file(file_path1)
    # data2 = parse_file(file_path2)
    # diff = creat_diff(data1, data2)
    # file_path1 = json.load(open('/home/mi_sanity/python-project-50/tests/fixtures/file1.json'))
    # file_path2 = json.load(open('/home/mi_sanity/python-project-50/tests/fixtures/file2.json'))
    file_path1 = json.load(open('/home/mi_sanity/python-project-50/tests/fixtures/file1.yml'))
    file_path2 = json.load(open('/home/mi_sanity/python-project-50/tests/fixtures/file2.yml'))
    # diff = creat_diff(file_path1, file_path2)
    diff = build_diff(file_path1, file_path2)
    return diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    diff = generate_diff(file_path1, file_path2)
    print('{', diff.lower(), '}', sep='\n')


if __name__ == '__main__':
    main()
