from functools import wraps


def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


@uppercase
def say_hello(name):
    """ This functions greets everyone

    """
    return f'Hello, {name}!'


@uppercase
def say_goodbye():
    """ This function wish you farewell

    """
    return 'Bye~'


# yell_hello = uppercase(say_hello)
# yell_goodbye = uppercase(say_goodbye)


print(say_hello('Garo'))
print(say_goodbye())
