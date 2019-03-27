from collections import defaultdict


def anagram(str1, str2):
    freq1 = defaultdict(str)
    freq2 = defaultdict(str)

    for char in str1:
        freq1[char] += 1
    for char in str2:
        freq2[char] += 1
    return freq1 == freq2
