numbers = [4, 5, 7, 1, 6]


def sq(num):
    return num**2


def check_for_five(num):
    return num > 5


sq_numbers = [num**2 for num in numbers]
sq_numbers = [sq(num) for num in numbers]
sq_numbers = list(map(sq, numbers))
print(sq_numbers)


more_than_five = [num for num in numbers if num > 5]
print(more_than_five)

print(list(filter(check_for_five, numbers)))
