from gendiff.cli import cli_args
from gendiff.generate_diff import generate_diff


def main():
    file1, file2, format_name = cli_args()
    diff = generate_diff(file1, file2, format_name)
    print(diff)


if __name__ == '__main__':
    main()
