import os


def open_my_file(filename):
    """

    Raises
    ------
    FileNotFoundError

    """
    if os.path.exists('test.py'):
        open('test.py')
    else:
        raise FileNotFoundError('Your file not found')


try:
    x = int(input('Enter number: '))

    y = 6 / x

    print(y)

    open_my_file('test.py')

except ZeroDivisionError:
    print('Do not enter 0')
except ValueError:
    print('Enter only numbers')
    exit()
except FileNotFoundError:
    raise Exception('I\'m not working anymore')
finally:
    print('finally test')
