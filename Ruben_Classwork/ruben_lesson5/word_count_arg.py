import sys
import os


if len(sys.argv) < 2:
    print("Please, provide file name")
    exit()

file_name = sys.argv[1]


bombs = []

with open(file_name, 'r') as fh:
    for line in fh:
        bombs.append(tuple(map(int, line.strip().split())))

print(bombs)

with open(f'{file_name}_new', 'w') as fh:
    for bomb in bombs:
        fh.write(f'{bomb[0]} -> {bomb[1]}\n')

print(os.getcwd())

os.chdir('./data_files')

print(os.getcwd())

for path, dirs, files in os.walk('.'):
    print(path, dirs, files)
