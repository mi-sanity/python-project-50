import argparse
from gendiff.scripts.parser import parse_file
from gendiff.scripts.build_diff import build_diff
from gendiff.formatters.stylish import stylish


FORMAT_NAMES = {
    'stylish': stylish
}


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    diff = build_diff(data1, data2)
    if isinstance(format_name, str):
        format_name = FORMAT_NAMES[format_name]
    diff = format_name(diff)
    return diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    file1 = args.first_file
    file2 = args.second_file
    format_name = args.format
    diff = generate_diff(file1, file2, format_name)
    print(diff)


if __name__ == '__main__':
    main()
