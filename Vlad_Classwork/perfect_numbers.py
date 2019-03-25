while True:
    top = input('Input the number: ')
    if top.isdecimal():
        top = int(top)
        break
    print('[ERROR] Invalid input')

for num in range(3, top + 1):
    if sum(n for n in range(1, num) if num % n == 0) == num:
        print(num, "is perfect")
