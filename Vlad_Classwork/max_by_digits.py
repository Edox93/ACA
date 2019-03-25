import random


def max_by_digits(arr: list) -> int:
    tmp = []
    for item in arr:
        tmp.append(sum(int(digit) for digit in str(item)))

    local = tmp[0]
    idx = 0
    for i in range(1, len(tmp)):
        if tmp[i] > local:
            local = tmp[i]
            idx = i


    local_max = 0
    result = 0
    for number in arr:
        sum_of_digits = sum(int(digit) for digit in str(item))
        if sum_of_digits > local_max:
            local_max = sum_of_digits
            result = number
        
    return arr[idx]


arr = random.sample(range(10, 30), 5)
print(arr)
print(max_by_digits(arr))
print(max(arr, key=lambda x: sum(map(int, str(x)))))
