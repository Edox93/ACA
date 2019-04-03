import argparse


parser = argparse.ArgumentParser()
parser.add_argument('text_input.txt')
args = parser.parse_args()
with open(args.filename) as file:
    text_my = file.read()
    print(text_my)
