while True:
    letter = input("please unput a letter")
    if len(letter) != 1:
        print("Please input only letter")
        continue

    if not letter.isalpha():
        print("Please input only latin letter")
        continue
    break

if letter.isupper():
    print('letter is uppercase')
else:
    print('letter is undercase'))
