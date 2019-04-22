# print( h_letters)
h_letters = [letter for letter in 'human']
print(h_letters)  # ['h', 'u', 'm', 'a', 'n']

# Using Lambda functions inside List
letters = list(map(lambda x: x, 'human'))
print(letters)  # ['h', 'u', 'm', 'a', 'n']

# Using if with List Comprehension
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# if...else With List Comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)  # ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
