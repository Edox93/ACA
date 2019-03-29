def f_cls_to_kvn(celsius):
    kelvin = celsius + 273.15
    return round(kelvin, 2)


def f_cls_to_fht(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return round(fahrenheit, 2)


def f_kvn_to_cls(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)


def f_kvn_to_fht(kelvin):
    fahrenheit = kelvin * (9 / 5) - 459.67
    return round(fahrenheit, 2)


def f_fht_to_cls(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return round(celsius, 2)


def f_fht_to_kvn(fahrenheit):
    kelvin = (fahrenheit + 459.67) * (5 / 9)
    return round(kelvin, 2)


print('Supported temperature formats: 36.6 C | 97.88 F | 309.75 K')
user_input = input('Temperature: ').upper()
temp_args = ('F', 'K', 'C')
user_input_list = user_input.split()
convert_to = input('Convert to (C(elsius) | K(elvin) | F(ahrenheit)): ').upper()
if len(user_input_list) == 2:

    if user_input_list[0].isnumeric():
            if user_input_list[0].isdigit() and \
                    user_input_list[-1].isalpha() and \
                    user_input_list[-1] == temp_args[-1] and \
                    len(convert_to) == 1 and \
                    convert_to == temp_args[0]:
                print(f_cls_to_fht(int(user_input_list[0])))
            else:
                print('invalid int')

            if user_input_list[0].isdigit() and \
                    user_input_list[-1].isalpha() and \
                    user_input_list[-1] == temp_args[-2] and \
                    len(convert_to) == 1 and \
                    convert_to == temp_args[1]:
                print(f_cls_to_fht(int(user_input_list[0])))
            else:
                print('invalid int')

            if user_input_list[0].isdigit() and \
                    user_input_list[-1].isalpha() and \
                    user_input_list[-1] == temp_args[-3] and \
                    len(convert_to) == 2 and \
                    convert_to == temp_args[2]:
                print(f_cls_to_fht(int(user_input_list[0])))
            else:
                print('invalid int')

    if not user_input_list[0].isalpha():
            if user_input_list[-1].isalpha() and \
                    user_input_list[-1] == temp_args[-1] and \
                    len(convert_to) == 1 and \
                    convert_to == temp_args[0]:
                print(f_cls_to_fht(float(user_input_list[0])))
            else:
                print('invalid float')

            if user_input_list[0].isdigit() and \
                    user_input_list[-1].isalpha() and \
                    user_input_list[-1] == temp_args[-2] and \
                    len(convert_to) == 1 and \
                    convert_to == temp_args[1]:
                print(f_cls_to_fht(int(user_input_list[0])))
            else:
                print('invalid int')

            if user_input_list[0].isdigit() and \
                    user_input_list[-1].isalpha() and \
                    user_input_list[-1] == temp_args[-3] and \
                    len(convert_to) == 2 and \
                    convert_to == temp_args[2]:
                print(f_cls_to_fht(int(user_input_list[0])))
            else:
                print('invalid int')

else:
    print('invalid number in list')
