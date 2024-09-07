# Usage
##  python3 argparse_named_arguments.py -f devatha  -l puneeth -y 2000

import argparse

parser = argparse.ArgumentParser(  
    description='Prints the person details')

# if dest is not provided then value is stored in the long flag, if long flag is not provided then value stored in short flag
parser.add_argument('-f', '--first-name', type=str, dest="first_name", help="first name", required=True)
parser.add_argument('-l', '--last-name', type=str, dest="last_name", help="last name")
parser.add_argument('-y', '--yob', type=int, dest="birth_year", help="date of birth", required=True)

args = parser.parse_args()

fullname = [args.first_name]
if args.last_name:
    fullname.append(args.last_name)
    
fullname = " ".join(fullname)
print(f"{fullname} born in {args.birth_year}")