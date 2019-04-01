def add(a, b):
    return a + b


def sub(a, b):
    return a - b


OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    'add': add
}
OPERATIONS['add'] = OPERATIONS['+']
OPERATIONS['sub'] = OPERATIONS['-']

STR_OPS = {
    '+': 'add',
    '-': 'sub',
    'add': 'add'
}

while True:
    tokens = input('Give me some expression: ').split()

    if len(tokens) != 3:
        print('Invalid expression format')
        continue

    if tokens[0] not in OPERATIONS:
        print('Invalid operation')
        continue

    ok = True
    for idx in range(1, 3):
        num = tokens[idx].lstrip('-')
        if num.isdecimal():
            tokens[idx] = int(tokens[idx])
        elif num.replace('.', '', 1).isdecimal():
            tokens[idx] = float(tokens[idx])
        else:
            ok = False
            print('Invalid number at position', idx)
            break

    if ok:
        break
    

if tokens[0] == '+' or tokens[0] == 'add':
    print(tokens[1] + tokens[2])
elif tokens[0] == '-' or tokens[0] == 'sub':
    print(tokens[1] - tokens[2])

print(OPERATIONS[tokens[0]](tokens[1], tokens[2]))
globals()[STR_OPS[tokens[0]]](tokens[1], tokens[2])

print(eval(f'{tokens[1]} {tokens[0]} {tokens[2]}'))
