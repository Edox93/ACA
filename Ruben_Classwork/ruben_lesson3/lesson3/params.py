def calc_sum(*args):
    buffer = 0

    print(args)

    for arg in args:
        buffer += arg

    return buffer


def calc_point_sum(a, b):
    return a + b


point = [6, 7]
calc_point_sum(*point)

numbers = [0, 5, 6, 1, 436]

res = calc_sum(4, 5, 6, 56, 56, 7, 27)

res1 = calc_sum(*numbers)

print(res)
print(res1)
