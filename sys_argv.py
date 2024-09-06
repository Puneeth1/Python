# python3 cli.py --first-name puneeth --last-name devatha
import sys

keys = sys.argv[1::2]
values = sys.argv[2::2]

args = { key:value for key, value in zip(keys, values) }

print(args.get('--first-name'))