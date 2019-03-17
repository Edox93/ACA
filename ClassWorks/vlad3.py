while True:
    num = input('Hit me:')
    if num.isdigit():
        break
    print('Give me a number')

sum_of_odds = 0
for n in range(int(num)):
    if n % 2 != 0:
        sum_of_odds += n


print(sum_of_odds)