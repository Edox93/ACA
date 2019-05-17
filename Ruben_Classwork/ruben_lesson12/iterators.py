class Fruits:
    def __init__(self):
        self.__items = ['apple', 'banana', 'pear']
        self.__counts = [5, 6, 10]

        self.x = 0
        self.y = 0
        self.z = 0

    def __iter__(self):
        for idx, item in enumerate(self.__items):
            yield (item, self.__counts[idx])

        # self.__idx = 0

    def __next__(self):
        if self.__idx == len(self.__items):
            raise StopIteration()

        item = (self.__items[self.__idx],
                self.__counts[self.__idx])
        self.__idx += 1

        return item

    def get_items(self):
        return self.__items


fruits = Fruits()

for fruit, count in fruits:
    print(fruit, count)

for fruit in fruits:
    print(fruit)

exit()


numbers = [5, 6, 7, 2, 4, 1]

print(numbers)

"""
for num in numbers:
    print(num)
"""

# num_iter = numbers.__iter__()
num_iter = iter(numbers)

num_iter.__next__()
x = next(num_iter)
print(x)
x = next(num_iter)
print(x)
x = next(num_iter)
print(x)
x = next(num_iter)
print(x)
x = next(num_iter)
print(x)
x = next(num_iter)
print(x)
x = next(num_iter)
print(x)
