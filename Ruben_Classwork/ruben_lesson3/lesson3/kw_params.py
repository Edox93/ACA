def name_printer(name='Artavazd'):
    print(name)


def fruit_printer(**kwargs):
    for key, arg in kwargs.items():
        print(f'{key} -> {arg}')


name_printer('Anushavan')
name_printer(name='Anushavan')

fruit_printer(apple=1, lemon=14, pear=8)


fruits = {'apple': 10, 'lemon': 0, 'pear': 80}
fruit_printer(**fruits)

print((4, *[6, 7], 5))

market = {'carrot': 25, 'potato': 100, **fruits, 'zuccero': 45}
print(market)
