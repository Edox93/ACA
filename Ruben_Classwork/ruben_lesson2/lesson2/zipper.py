names = ['Artavazd', 'Garegin']
surnames = ['Qartashyan', 'Zhamkochyan']
suffix = ['Jr.', '']

for name, surname, suf in zip(names, surnames, suffix):
    print(name, surname, suf)


numbers = (1, 4, 1, 3, 6, 8)

first, second, *others, last = numbers

new_numbers = (10, 5, *others, 24, 56)
print(new_numbers)
