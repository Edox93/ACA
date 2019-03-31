while True:
    a = input('input:')
    if not a.isalpha() and not a.isdecimal() and '.' in a and '.' != a[0] or '.' != a[-1]:
        a = float(a)
        print(type(a))
    elif a.isalpha():
        a = str(a)
        print(type(a))
    elif a.isdigit():
        a = int(a)
        print(type(a))
    else:
        print(type(a),  'i do not know')

