with open('text.txt') as file:
    data = file.read().replace('\n', '').replace('.', '').lower().split()
    result = {}
    new_result = {}
    for word in data:
        if result.get(word, 0) == 0:
            result[word] = 1
        else:
            result[word] += 1

    for i in sorted(result):
        print((i, result[i]), end=" ")

    # sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    # print(sorted_result[0:3])



    # key_max1 = max(result.keys(), key=(lambda k: result[k]))
    # print(key_max1)
    # # print(type(result[key_max1]))
    # # print(type(key_max1))
    # new_result.update({key_max1: result[key_max1]})
    # del result[key_max1]
    # key_max2 = max(result.keys(), key=(lambda k: result[k]))
    # # print(result[key_max2])
    # # print(key_max2)
    # new_result.update({key_max2: result[key_max2]})
    # del result[key_max2]
    # key_max3 = max(result.keys(), key=(lambda k: result[k]))
    # # print(result[key_max3])
    # # print(key_max3)
    # new_result.update({key_max3: result[key_max3]})
    # # new_result[key_max1] = result[key_max1]
    # # new_result[key_max2] = result[key_max2]
    # # new_result[key_max3] = result[key_max3]
    # print(new_result)
    #
    # # value = result.values()
    # # keys = result.keys()
    #
    # # max_element = max(zip(result.values(), result.keys()))
    # # print(zip(result.values(), result.keys()))
