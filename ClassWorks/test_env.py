print('hello', 'world', sep='\n')
print('hello', 'world', sep='*')
print('hello', 'world', sep='')
print('bye world')
print('insert a digit', int(input('only digits:'))+1)


user_input = int(input('enter a decimal digit:'))

while not user_input.isdecimal():
    user_input = input('invalid input')

while True:
    user_input = input('invalid input')
    if user_input.isdecimal():
        break
    if not user_input.isdecimal():
        print('invalid input')
print(user_input, " 1", int(input(user_input)) + 1)






