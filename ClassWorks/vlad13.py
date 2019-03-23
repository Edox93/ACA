def max_by_digits(*args) -> int:
    for input_digit in args:
        input_digit = str(input_digit)
        total = 0
        my_list = list()
        for letter in str(input_digit):
            total += int(letter)
            my_list.append(total)
            return my_list



print(max_by_digits(10, 12, 7, 9, 111))  # 9





