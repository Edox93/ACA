def factorial(top: int) -> int:
    result = 1
    for n in range(2, top + 1):
        result *= n
    return result


def rec_factorial(top: int) -> int:
    if top <= 1:
        return 1
    return top * rec_factorial(top - 1)


def fib(pos: int) -> int:
    prev, curr = 1, 1
    for idx in range(pos - 2):
        prev, curr = curr, curr + prev
    return curr


def rec_fib(pos: int) -> int:
    if 1 <= pos <= 2:
        return 1
    return rec_fib(pos - 1) + rec_fib(pos - 2)
