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
for bracket in user_input:
    if bracket in brackets_left:
        new_brackets.append(bracket)
    elif bracket in brackets_right:
        bracket_index = brackets_right.index(bracket)  # 0, 1, 2
        if len(new_brackets) > 0 and new_brackets[len(new_brackets) - 1] == brackets_left[bracket_index]:
            new_brackets.pop()
        else:
            print("Invalid")
            exit()

if len(new_brackets) == 0:
    print("Valid")


# Line17   -->   length - 1 == last iterated element for compaire

# {([])]}{}
# ([]{}{}())
# ({}[)]()

# {([])]}{}
# {()]}{}
# {]}{}
# {]}
# False

# ({[()]}[])
# ({[]}[])
# ({}[])
# ([])
# ()
#
# True
