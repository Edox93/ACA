import sys


def add(operand1, operand2):
        add_result = operand1 + operand2
        return add_result


def sub(operand1, operand2):
        sub_result = operand1 - operand2
        return sub_result


def mul(operand1, operand2):
        mul_result = operand1 - operand2
        return mul_result


def div(operand1, operand2):
        div_result = operand1 - operand2
        return div_result


user_input = input('please input like this expression: operator operand operand:').split()
operators_list = ('+', 'add', '-', 'sub', '*', 'mul', '/', 'div')
if len(user_input) != 3:
    print('Invalid Input style')
    sys.exit()

if user_input[0] not in operators_list:
    print('Invalid operator')
for input_str in range(1, 3):
    number = user_input[input_str].lstrip('-')
    if number.isdecimal():
        user_input[input_str] = int(user_input[input_str])
    elif number.replace('.', '', 1).isdecimal():
        user_input[input_str] = float(user_input[input_str])
    else:
        print('Invalid number at position', input_str)


if user_input[0] == operators_list or user_input[0] == operators_list[1]:
    print(add(user_input[1], user_input[2]))
if user_input[0] == operators_list[2] or user_input[0] == operators_list[3]:
    print(add(user_input[1], user_input[2]))
if user_input[0] == operators_list[4] or user_input[0] == operators_list[5]:
    print(add(user_input[1], user_input[2]))
if user_input[0] == operators_list[6] or user_input[0] == operators_list[7]:
    print(add(user_input[1], user_input[2]))
