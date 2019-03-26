text_list = list()
text_string = str()
text_dict = dict()


with open('text.txt') as file:
    data = file.read().replace('\n', '')
    print(data)
