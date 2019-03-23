#def foo(a: int, b: str, c: object, *args: tuple, **kwargs: dict) -> str:
#    return "baz"

#def foo(firs: int, *args: tuple, **kwargs: dict) -> str
#   print('first:', firs)
#    print("args:", args)

#if __name__ == "__main__":
#    foo(1, 2, 3, 4, 5, secoond = 123)


def foo(firs: int, *args: tuple, **kwargs: dict) -> tuple:
    return 'a', 1, 123, {}

#if __name__ == '__main__':
    f, s, t, f = foo(1, 2, 4, 5, second=123)
    print(s)
