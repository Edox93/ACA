def add(operator, operand1, operand2):
    if operator == '+' or operator == 'add':
        add_result = operand1 + operand2
        return add_result


def sub(operator, operand1, operand2):
    if operator == '-' or operator == 'sub':
        sub_result = operand1 - operand2
        return sub_result


def mul(operator, operand1, operand2):
    if operator == '*' or operator == 'mul':
        mul_result = operand1 - operand2
        return mul_result


def div(operator, operand1, operand2):
    if operator == '/' or operator == 'div':
        div_result = operand1 - operand2
        return div_result


user_input = input('please input like this expression: operator operand operand:').split()
operators_list = ['+', 'add', '-', 'sub', '*', 'mul', '/', 'div']
if len(user_input) != 3 and user_input[0] not in operators_list:
    print('Invalid operator and count of inputs')

    if user_input[0] == user_input[1] or user_input[0] == user_input[2]:
        print('operator cannot be operand or vice versa')


