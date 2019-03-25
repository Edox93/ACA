text_list = list()
text_string = str()
text_dict = dict()

with open('text.txt') as file:
    for word in file:
        data = word.split()
        for multi_word in data:
            if multi_word in data:
                print(multi_word)
