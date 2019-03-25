birthdate = '2018_04_10'

dates = birthdate.split('_')
print(dates)
print("-".join(dates))

name = ['John', 'Black', 'Jr.']

print("{} {}".format(name[0], name[1]))
print(" ".join(name))

# print(" ".join())

numbers = [3, 5, 7, 1]

print("-".join([str(num) for num in numbers]))
