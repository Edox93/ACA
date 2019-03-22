def f_calc(operator, operand1, operand2):
    if type(operand1) is int or type(operand1) is float:
        if type(operand2) is int or type(operand2) is float:
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
            return "invalid operand1"
    else:
        return "invalid operand1"


operator_out = input("please insert an operator:")
operand1_out = input("please insert an operand1:")
operand2_out = input("please insert an operand2:")
print(f_calc(operator_out, operand1_out, operand2_out))
