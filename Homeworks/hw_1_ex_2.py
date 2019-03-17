while True:
    char = input('enter a letter:').lower()
    vowel = ['a', 'e', 'i', 'o', 'u']
    if len(char) == 1 and char.isalpha():
        if char in vowel:
            print("the letter is vowel")
        else:
            print("the letter isn't vowel")
    else:
        print('The', char, "is invalid input")
