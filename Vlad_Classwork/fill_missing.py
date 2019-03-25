""" Fill the string with specified character """

def pad_left(txt: str, length: int, char: str) -> str:
    return '{}{}'.format(char * (length - len(txt)), txt)


def pad_right(txt: str, length: int, char: str) -> str:
    return '{1}{0}'.format(char * (length - len(txt)), txt)


while True:
    length = input('Length: ')
    if length.isdecimal():
        length = int(length)
        break
    print('[ERROR] Please insert a number for length')

while True:
    fill = input('Fill: ')
    if len(fill) == 1:
        break
    print('[ERROR] Please insert one symbol for fill')

txt = input('Text: ')

print(pad_left(txt, length, fill))
