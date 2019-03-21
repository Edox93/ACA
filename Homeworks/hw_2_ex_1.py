while True:
    user_input = input('Please input an integer')
#    perfect_count = False
    if user_input.isdecimal():
        user_input = int(user_input)
        for digit in range(1, user_input):
            sum_divisible = 0
            for every_digit in range(1, (digit // 2) + 1):
                if digit % every_digit == 0:
                    sum_divisible = sum_divisible + every_digit
            if sum_divisible == digit:
#           if perfect_count is True:
                print(sum_divisible)
#            if perfect_count is False:
#                print('No perfect numbers in this range')
    else:
        print('Invalid input')
