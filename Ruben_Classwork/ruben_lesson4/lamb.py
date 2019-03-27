

from functools import reduce


numbers = [3, 4, 7, -4, 7, 71, 9, 1]


print(reduce(lambda x, y: x - y, numbers))


print([num ** 2 for num in numbers])

print(list(map(lambda num: num ** 2, numbers)))
