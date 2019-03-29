# Validate brackets in any given expression, for example:
# ((){[()]}[]) is valid
# 5 - (6 + [4 5]/8) + {4 - 5 (18 - 4)} is valid
# ([)]{()[}] is invalid
# (a * 2 - (b + [4 -8)] + {12 / (34 - 56)}) is invalid
my_string = '(a * 2 - (b + [4 -8)] + {12 / (34 - 56)})'
brackets = ['(', ')', '[', ']', '{', '}']
my_sorted_brackets = []
for i in my_string:
    if i in brackets:
        my_sorted_brackets.append(i)
print(my_sorted_brackets)
if my_sorted_brackets[0] == brackets[0] and my_sorted_brackets[-1] == brackets[1]:
    print('it is ( )')
if my_sorted_brackets[0] == brackets[2] and my_sorted_brackets[-1] == brackets[3]:
    print('it is [ ]')
if my_sorted_brackets[0] == brackets[4] and my_sorted_brackets[-1] == brackets[5]:
    print('it is { }')


