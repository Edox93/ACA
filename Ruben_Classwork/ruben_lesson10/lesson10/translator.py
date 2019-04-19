import json


class Symbol:
    def __init__(self, code, is_digit):
        self.code = code
        self.is_digit = is_digit

    def __repr__(self):
        return '\n{0[0]}{0[1]}\n{1[0]}{1[1]}\n{2[0]}{2[1]}\n'.format(
            self.code[0], self.code[1], self.code[2])

    def isdigit(self):
        return self.is_digit


class Translator:
    def __init__(self, data: str, alphabet_path: str):
        self.data = data

        self.braille = []
        self.mapping = {}

        self.read_alphabet(alphabet_path)

    def read_alphabet(self, path):
        symbols = json.load(open(path))
        for key, code in symbols.items():
            self.mapping[key] = Symbol(code, key.isdigit())

    def translate(self):
        # translate from english to braille
        for letter in self.data:
            idx = len(self.braille)
            self.braille.extend(self.__translate_letter(letter, idx))

    def __translate_letter(self, letter: str, idx: int) -> list:
        res = []

        prev_letter = self.braille[idx - 1] if idx != 0 else None
        if letter.isdigit() and not prev_letter.isdigit():
            res.append(self.mapping['num'])

        res.append(self.mapping[letter])

        return res

    def get_translation(self):
        return self.braille
