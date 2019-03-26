text_string = str()
text_dict = dict()

with open('text.txt') as file:
    data = file.read().replace('\n', '')
    data = data.replace('.', '')
    data = data.lower()
    data = data.split()
print(data)


