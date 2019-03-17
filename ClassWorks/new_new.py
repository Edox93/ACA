first = 'hello '
second = 'world'
result = '{} {}'.format(first, second)
result1 = '{1} {0}'.format(first, second)
print(result)
print(result1)

print('{:.3f}'.format(3.42353465))
print(type(123))
print(isinstance(123, int))
print(isinstance(123, (int, float)))

a = input()
isinstance(a, (list, tuple, set, dict))
