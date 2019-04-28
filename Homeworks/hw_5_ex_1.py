def type_check(type_func):
    def wrap(function):
        def value_checker(*args):
            for arg in args:
                if type(arg) is not type_func:
                    print("type error message")
                    break
                # elif type(arg) is type_func:
                #     print('type checked and there is not found type errors')
                #     break
            function(*args)
        return value_checker
    return wrap


@type_check(str)
def check_values(a, b, c):
    return "a, b, c"


if __name__ == '__main__':
    check_values('1', '2', '3')
