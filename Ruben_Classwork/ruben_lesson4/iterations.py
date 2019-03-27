

# import itertools
from itertools import cycle, chain, compress


for number in cycle([0, 1]):
    print(number)

    if number == 1:
        break


fruits = ['apple', 'pear']
vegitables = ['potato', 'cabbage']

all = [fruits, vegitables]

for thing in chain.from_iterable(all):
    print(thing)

data = 'potato'
selector = [True, False, True]

print(data)
print(selector)
for sel in compress(data, selector):
    print(sel)


for idx, sel in enumerate(data):
    if idx < len(selector) and selector[idx]:
        print(sel)
