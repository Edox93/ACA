provided_list = ["1", 1, "abc", 123, 124.6, ['123', 1, 45], (1, 2), 3456, 567]
integer_list = list()
for instance in provided_list:
    if type(instance) == int:
        integer_list.append(instance)
    elif type(instance) == list or type(instance) == tuple:
        for list_int in instance:
            if type(list_int) == int:
                integer_list.append(list_int)
#    elif type(instance) == tuple:
#        for tuple_int in instance:
#            if type(tuple_int) == int:
#                integer_list.append(tuple_int)
print('the count of integers in provided_list is:', len(integer_list))
