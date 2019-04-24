def text_to_braille(text_input):
    result = ""
    for char in text_input:
        value = letter_to_braille(char)
        for v in value:
            for f in v:
                if f == 1:
                    charBraille = 'o'
                else:
                    charBraille = '-'
                print(charBraille, end='')
            print('')
        # print('', end='')

    return result


def letter_to_braille(text_input):
    return braille.get(text_input)


def print_braille():
    print(text_to_braille("ab"))


braille = {'a': [[1, 0], [0, 0], [0, 0]],
           'b': [[1, 0], [1, 0], [0, 0]],
           'c': [[], [], []],
           'd': [[], [], []],
           'e': [[], [], []],
           'f': [[], [], []],
           'g': [[], [], []],
           'h': [[], [], []],
           'i': [[], [], []],
           'j': [[], [], []],
           'k': [[], [], []],
           'l': [[], [], []]
           }

print_braille()