def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


while True:
# Driver code
    string = input('please insert:')
    print(string, "-", matched(string))
