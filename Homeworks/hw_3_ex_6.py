def f_cls_to_kvn(celsius):
    kelvin = celsius + 273.15
    return kelvin


def f_cls_to_fht(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit


def f_kvn_to_cls(kelvin):
    celsius = kelvin - 273.15
    return celsius


def f_kvn_to_fht(kelvin):
    fahrenheit = kelvin * (9 / 5) - 459.67
    return fahrenheit


def f_fht_to_cls(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


def f_fht_to_kvn(fahrenheit):
    kelvin = (fahrenheit + 459.67) * (5 / 9)
    return kelvin


user_input = input('Please input a temperature: ')
temp_args = ('F', 'K', 'C')
to_convert = input('Convert to. for (C) please input C for (F) -> F, and for (K) -> K: ')
user_input_list = []
str_from_user_input_list = ''

user_input = user_input.replace(' ', '').upper()
if user_input[-1] in temp_args and user_input[0].isdigit() and user_input[-2].isdigit():
    for str_el in user_input:
        user_input_list.append(str_el)
else:
    print('invalid temperature input')
user_input_list.insert(-1, '')

#for i in range(len(user_input_list) - 2):
str_from_user_input_list = ''.join(str(e) for e in user_input_list)
str_from_user_input_list = str_from_user_input_list[:-1] + str_from_user_input_list[5:]
print(str_from_user_input_list)
if str_from_user_input_list.isdigit():
    print(type(int(str_from_user_input_list)))
elif str_from_user_input_list.isnumeric():
    print(type(float(str_from_user_input_list)))

