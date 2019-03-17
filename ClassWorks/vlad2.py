user_input = input('please input a int:')
if user_input.isdecimal():
    user_input = range(int(user_input))
    print(user_input)

else:
    print('your input was not a digit')

