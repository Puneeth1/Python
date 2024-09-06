import argparse

parser = argparse.ArgumentParser(
    description='sum the integers at the command line')

parser.add_argument("firstname", type=str)
parser.add_argument("lastname", type=str)

args = parser.parse_args()
print(f"Full name is {args.firstname} {args.lastname}")