with open('text.txt') as file:
    data = file.read().replace('\n', '').replace('.', '').lower().split()
    result = {}
    for word in data:
        if result.get(word, 0) == 0:
            result[word] = 1
        else:
            result[word] += 1
    print(result)

    # value = result.values()
    # keys = result.keys()

    # max_element = max(zip(result.values(), result.keys()))
    # print(zip(result.values(), result.keys()))
