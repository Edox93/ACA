shapes = {'triangle': 3, 'squere': 4, 'circle': 0}

fruits = dict([('apple', 14), ('pear', 20)])
print(fruits)

for shape, angles in shapes.items():
    print(shape, angles)

shapes['squere'] += 4

del shapes['squere']

shapes['octogon'] = 8

print(shapes.get('squere', 4))

print('squere' in shapes)

print(shapes.keys())
print(shapes.values())
