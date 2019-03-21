while True:
    operator_input = input('insert an operator:')
    operand1_input = input('insert an operand 1:')
    operand2_input = input('insert an operand 2:')
    all_operators = ['+', 'add', '-', 'sub', '*', 'mul', '/', 'div']
    if operator_input in all_operators:
        if operator_input is all_operators[1]:
            print(int(operand1_input) + int(operand2_input))
        elif operator_input is all_operators[2]:
            print(int(operand1_input) - int(operand2_input))
        elif operator_input is all_operators[4]:
            print(int(operand1_input) * int(operand2_input))
        elif operator_input is all_operators[6]:
            print(int(operand1_input) // int(operand2_input))
    else:
        print('invalid operator')

