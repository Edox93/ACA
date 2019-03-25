def adder(start, *args, **kwargs):
    buf = start

    op = kwargs.get('op', '+')

    for arg in args:
        if op == '+':
            buf += arg
        elif op == '-':
            buf -= arg
        else:
            print('Operation is not supported')

    return buf


print(adder(4, 5, 7, -4, op='-', cos='10'))
print(adder(4, 5, 7, -4, op='/', cos='10'))
print(adder(4, 5, 7, -4))
