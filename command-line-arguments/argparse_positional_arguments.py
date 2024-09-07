import argparse

parser = argparse.ArgumentParser(
    description='Prints the full name')

parser.add_argument("firstname", type=str)
parser.add_argument("lastname", type=str)

args = parser.parse_args()
print(f"Full name is {args.firstname} {args.lastname}")