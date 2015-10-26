import argparse
import random
import string

parser = argparse.ArgumentParser(description="""A small password generator.""")

parser.add_argument('length', metavar='length', type=int,
                    help='the password length')

args = parser.parse_args()

characters = string.ascii_lowercase\
           + string.ascii_uppercase\
           + string.digits\
           + '!@#$%^&*()'

print ''.join(random.choice(characters) for _ in range(args.length))
