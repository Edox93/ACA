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
valid_temperature_formats = ['F', 'K', 'C']
user_input_list = user_input.split()
convert_to = input('Convert to (C(elsius) | K(elvin) | F(ahrenheit)): ').upper()

if len(user_input_list) == 2 and (not user_input_list[0].isalpha()) and user_input_list[1].isalpha() \
        and (convert_to in valid_temperature_formats) and (user_input_list[1] in valid_temperature_formats):

    temperature = float(user_input_list[0])
    temperature_format = user_input_list[1]

    if temperature_format != convert_to:
        if temperature_format == 'C':
            if convert_to == 'K':
                print(user_input, '=', f_cls_to_kvn(temperature), 'K')
            if convert_to == 'F':
                print(user_input, '=', f_cls_to_fht(temperature), 'F')

        if temperature_format == 'K':
            if convert_to == 'C':
                print(user_input, '=', f_kvn_to_cls(temperature), 'C')
            if convert_to == 'F':
                print(user_input, '=', f_kvn_to_fht(temperature), 'F')

        if temperature_format == 'F':
            if convert_to == 'K':
                print(user_input, '=', f_fht_to_kvn(temperature), 'K')
            if convert_to == 'C':
                print(user_input, '=', f_fht_to_cls(temperature), 'C')
    else:
        print(user_input)
else:
    print('invalid number in list')
