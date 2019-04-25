import argparse


def text_to_braille(text_input):
    result = ""
    for char in text_input:
        br_char_list = letter_to_braille(char)
        for br_1_0 in br_char_list:
            for br_dot in br_1_0:
                if br_dot == 1:
                    br_char = 'o'
                else:
                    br_char = '-'
                print(br_char, end='')
            print('')
    return result


def letter_to_braille(text_input):
    return braille.get(text_input)


def print_braille():
    print(text_to_braille(input('please input your text for ceonverting to braille')))

# parser = argparse.ArgumentParser()
# parser.add_argument("-f", "--file", required=True, help="text file for converting to braille")
# args = parser.parse_args()
# with open(args.filename) as file:


braille = {'a': [[1, 0], [0, 0], [0, 0]],
           'b': [[1, 0], [1, 0], [0, 0]],
           'c': [[1, 1], [0, 0], [0, 0]],
           'd': [[1, 1], [0, 1], [0, 0]],
           'e': [[1, 0], [0, 1], [0, 0]],
           'f': [[1, 1], [1, 0], [0, 0]],
           'g': [[1, 1], [1, 1], [0, 0]],
           'h': [[1, 0], [1, 1], [0, 0]],
           'i': [[0, 1], [1, 0], [0, 0]],
           'j': [[0, 1], [1, 1], [0, 0]],
           'k': [[1, 0], [0, 0], [1, 0]],
           'l': [[1, 0], [1, 0], [1, 0]],
           'm': [[1, 1], [0, 0], [1, 0]],
           'n': [[1, 1], [0, 1], [1, 0]],
           'o': [[1, 0], [0, 1], [1, 0]],
           'p': [[1, 1], [1, 0], [1, 0]],
           'q': [[1, 1], [1, 1], [1, 0]],
           'r': [[1, 0], [1, 1], [1, 0]],
           's': [[0, 1], [1, 0], [1, 0]],
           't': [[0, 1], [1, 1], [1, 0]],
           'u': [[1, 0], [0, 0], [1, 1]],
           'v': [[1, 0], [1, 0], [1, 1]],
           'w': [[0, 1], [1, 1], [0, 1]],
           'x': [[1, 1], [0, 0], [1, 1]],
           'y': [[1, 1], [0, 1], [1, 1]],
           'z': [[1, 0], [0, 1], [1, 1]],
           '1': [[1, 0], [0, 0], [0, 0]],
           '2': [[1, 0], [1, 0], [0, 0]],
           '3': [[1, 1], [0, 0], [0, 0]],
           '4': [[1, 1], [0, 1], [0, 0]],
           '5': [[1, 0], [0, 1], [0, 0]],
           '6': [[1, 1], [1, 0], [0, 0]],
           '7': [[1, 1], [1, 1], [0, 0]],
           '8': [[1, 0], [1, 1], [0, 0]],
           '9': [[0, 1], [1, 0], [0, 0]],
           '0': [[0, 1], [1, 1], [0, 0]],
           'space': [[0, 0], [0, 0], [0, 0]],
           'number': [[0, 1], [1, 1], [0, 0]],
           'letter': [[0, 0], [0, 1], [0, 1]],

           }

print_braille()
