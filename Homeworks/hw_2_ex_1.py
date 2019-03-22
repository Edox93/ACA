while True:
    user_input = input('Please input an integer')
    have_perfect_number = False
    if user_input.isdecimal():
        user_input = int(user_input)
        for digit in range(1, user_input):
            sum_divisible = 0
            for every_digit in range(1, (digit // 2) + 1):
                if digit % every_digit == 0:
                    sum_divisible = sum_divisible + every_digit
            if sum_divisible == digit:
                have_perfect_number = True
                print(sum_divisible)
        if have_perfect_number == False:
            print('No Perfect Number')
        break
    else:
        print('Invalid input')
