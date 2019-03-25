numbers = [1, 4, 5, 0, 4, 5]

fruits = {'apple': 4, 'banana': 6}

res = []

for number in numbers:
    if number > 3:
        res.append(number)

res = [count + 1 if fruit == 'apple' else count + 3
       for fruit, count in fruits.items()]

print(res)

squeres = {num: num**2 for num in numbers}
squeres = {f.upper(): c**2 for f, c in fruits.items()}
print(squeres)

name = 'Artavazd'
res = 'Yes' if name == 'Garegin' else 'No'
print(res)
