from collections import defaultdict


def anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    word_one_dict = defaultdict(int)
    word_two_dict = defaultdict(int)

    for char in str1:
        word_one_dict[char] += 1
    for char in str2:
        word_two_dict[char] += 1
    return word_one_dict == word_two_dict


word1 = input('please insert word 1:')
word2 = input('please insert word 2:')
print(anagram(word1, word2))
