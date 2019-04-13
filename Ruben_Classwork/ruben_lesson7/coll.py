import collections
from rand import generate_pwd


fruits = collections.OrderedDict([('apple', 4), ('pear', 10)])

# print(fruits['apple'])


data = generate_pwd(1000)

lc = collections.defaultdict(int)

for letter in data:
    lc[letter] += 1

print(lc)
