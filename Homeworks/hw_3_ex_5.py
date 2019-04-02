# Validate brackets in any given expression, for example:
# ((){[()]}[]) is valid
# 5 - (6 + [4 5]/8) + {4 - 5 (18 - 4)} is valid
# ([)]{()[}] is invalid
# (a * 2 - (b + [4 -8)] + {12 / (34 - 56)}) is invalid
from sys import exit

user_input = input('please enter your expression: ')
brackets_left = ('(', '[', '{')
brackets_right = (')', ']', '}')
new_brackets = []
for i in user_input:
    if i in brackets_left:
        new_brackets.append(i)
    elif i in brackets_right:
        bracketPosition = brackets_right.index(i)
        if len(new_brackets) > 0 and new_brackets[len(new_brackets) - 1] == brackets_left[bracketPosition]:
            new_brackets.pop()
        else:
            print("Invalid")
            exit()

if len(new_brackets) == 0:
    print("Valid")

# {([])]}{}
# ([]{}{}())
# ({}[)]()