text_list = list()
text_string = str()
with open('text.txt') as file:

    for line in file:
        text_list.append(line)
print(text_list)

