import argparse

def get_help_gendiff():
    parser = argparse.ArgumentParser(
        prog='gendiff', 
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.print_help()
