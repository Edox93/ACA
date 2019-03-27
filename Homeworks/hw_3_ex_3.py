from collections import Counter

with open('text.txt') as file:
    data = file.read().replace('\n', '').replace('.', '').lower().split()
    result = {}
    new_result = {}
    for word in data:
        if result.get(word, 0) == 0:
            result[word] = 1
        else:
            result[word] += 1

frequent_words = Counter(result)
first_three_frequent_words = frequent_words.most_common(3)
print(first_three_frequent_words)
