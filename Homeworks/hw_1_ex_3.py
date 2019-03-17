data = input('please insert a hash:')
upper_letters = list()
lower_letters = list()
digits = list()
for i in data:
    if i.isalpha():
        if i.isupper():
            upper_letters.append(i)
        else:
            lower_letters.append(i)
    else:
        digits.append(i)
result = [lower_letters, digits, upper_letters]
print(result)
