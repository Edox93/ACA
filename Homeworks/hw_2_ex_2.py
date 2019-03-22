def f_calc(operator, operand1, operand2):
    if type(operand1) is int or type(operand1) is float and type(operand2) is int or type(operand2) is float:
        if operator == '+' or operator == "add":
            return operand1 + operand2
        elif operator == '-' or operator == "sub":
            return operand1 - operand2
        elif operator == '*' or operator == "mul":
            return operand1 * operand2
        elif operator == '/' or operator == "div":
            return operand1 // operand2
        else:
            return 'invalid operator'
    else:
        return "invalid operand1 or operand2"


operator_out = input("please insert an operator:")

#if operator_out == '+' or operator_out == 'add'

operand1_out = input("please insert an operand1:")
if not operand1_out.isalpha():
    if operand1_out.isnumeric():
        i = int(operand1_out)
        print("int")
    else:
        f = float(operand1_out)
        print("float")

operand2_out = input("please insert an operand2:")
if not operand2_out.isalpha():
    if operand2_out.isnumeric():
        i = int(operand2_out)
        print("int")
    else:
        f = float(operand2_out)
        print("float")

#
#print(f_calc(operator_out, operand1_out, operand2_out))
