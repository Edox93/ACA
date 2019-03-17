user_input = input('insert a one char')
if len(user_input) == 0 and user_input.isalpha():
    print("please insert a one character")
else:
    if user_input.isupper():
        print('your char is upper')
    else:
        print('your char is under')





