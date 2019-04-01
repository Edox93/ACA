def pig_it(text: str) -> str:
    return ' '.join(('{}{}ay'.format(word[1:], word[0]) if word.isalpha() else word for word in text.split()))


if __name__ == '__main__':
    print('this is a long text, which contains different words!')
    print(pig_it('this is a long text, which contains different words!'))
