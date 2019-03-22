a = input()

if a.isnumeric():
    if a.isdigit():
        a = int(a)
        print('int', a)
    else:
        a = float(a)
        print('float', a)
else:
    print("input is not int or float")
