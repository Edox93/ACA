numbers = [1, 3, 6, 13, 21, 4, 9, 78, 34, 55, 4, 10]
ten_and_above = list()
bellow_from_ten = list()
for number in numbers:
    if number >= 10:
        ten_and_above.append(number)
    else:
        bellow_from_ten.append(number)
print('bellow_from_ten =', bellow_from_ten, ",", 'ten_and_above =', ten_and_above)
