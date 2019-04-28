from datetime import datetime


def my_decorator(func):
    def wrapper():
        start = datetime.now()
        result = func
        print(datetime.now() - start)
        return result
    return wrapper()


@my_decorator
def one():
   # start = datetime.now()
    edgar = [number for number in range(10 ** 4) if number % 2 == 0]
   # print(datetime.now() - start)
    return edgar

@my_decorator
def two():
   # start = datetime.now()
    edgar = []
    for number in range(10 ** 4):
        if number % 2 == 0:
            edgar.append(number)
   # print(datetime.now() - start)
    return edgar


print(one())
print(two())
