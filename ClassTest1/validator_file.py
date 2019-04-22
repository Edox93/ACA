
def validator(txt_matrix):
    matrix = []
    unpack_matrix = []
    for item in txt_matrix.read().split('\n'):
        matrix.append(item.split())
    for i in matrix:
        unpack_matrix.append(*i)
    if len(unpack_matrix) == 10:
        for matrix_element in unpack_matrix:
            if len(matrix_element) == 10:
                for char_of_mat_element in matrix_element:
                    if char_of_mat_element == '0' or char_of_mat_element == '1':
                        pass

                    else:
                        print('invalid characters')
            else:
                print('invalid length of line')

    else:
        print('the matrix have lines more than 10')








# matrix_dict = collections.defaultdict(int)
# for m1 in matrix2:
#     for m in m1:
#         for d in m:
#             if int(d) == 1:
#                 matrix_dict[d] += 1
# print(matrix_dict)




#         matrix_dict[m] += 1
# print(matrix_dict[])





