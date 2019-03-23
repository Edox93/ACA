def alphabet_position(text: str) -> str:
    my_list = list()
    for elements in text:
        if elements.isalpha():
            my_list.append(ord(elements.lower()) - 96)
 #   return my_list
    return  

#print(*alphabet_position('dOh!'))     # 4 15 8
