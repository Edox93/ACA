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
