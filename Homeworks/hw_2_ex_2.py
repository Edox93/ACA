while True:
    operator_input = input('insert an operator:')
    operand1_input = input('insert an operand 1:')
    operand2_input = input('insert an operand 2:')
    if operator_input == '+' or 'add':
        sum_add = int(operand1_input) + int(operand2_input)
        print(sum_add)
    elif operator_input == '-' or 'sub':
        sum_sub = int(operand1_input) - int(operand2_input)
        print(sum_sub)
    elif operator_input == '*' or 'mul':
        sum_mul = int(operand1_input) * int(operand2_input)
        print(sum_mul)
    elif operator_input == '/' or 'div':
        sum_div = int(operand1_input) / int(operand2_input)
        print(sum_div)
    else:
        if operator_input != '+' or 'add' or '-' or 'sub' or '*' or 'mul' or '/' or 'div':
            print('invalid operator')
        if type(operand1_input) and type(operand2_input) != int or float:
            print('invalid operator')
