import argparse


parser = argparse.ArgumentParser()

parser.add_argument('op', choices=('+', '-', '*', '/'),
                    help='Mathematical operation')

parser.add_argument('numbers', nargs='+', type=float)

parser.add_argument('-f', '--file', action='store_const', const='result.txt',
                    help='Output to file')

args = parser.parse_args()

print(type(args.op), type(args.numbers))
print(args.op, args.numbers, args.file)

# polish_calculator(args.op, args.num1, args.num2)
