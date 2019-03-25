random_number = 15


def calc_sum(num1, num2, random_number):
    random_number = str(num1)
    return num1, num2, num1 + num2, random_number


arg1, arg2, _sum, random_number = calc_sum(4, 6, random_number)

print(random_number)

print(arg1, arg2, _sum)


def say_hi(surname, name='Artavazd', suffix=''):
    print(f'Hi, {surname} {name} {suffix}!')


say_hi('Makunc')
say_hi('Barkhudaryan', 'Termine', 'Jr.')
say_hi('Barkhudaryan', suffix='Jr.')
