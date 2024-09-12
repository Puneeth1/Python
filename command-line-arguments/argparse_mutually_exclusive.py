import argparse

parser = argparse.ArgumentParser(description='test mutually exclusive arguments')

group = parser.add_mutually_exclusive_group()

group.add_argument('--verbose', help="Verbose output", action="store_true")
group.add_argument('--quiet', help="Quiet output", action="store_true")

parser.add_argument('--test', help="Test parameter")


args = parser.parse_args()


## python3 argparse_mutually_exclusive.py --verbose --quiet
# usage: argparse_mutually_exclusive.py [-h] [--verbose | --quiet] [--test TEST]
# argparse_mutually_exclusive.py: error: argument --quiet: not allowed with argument --verbose