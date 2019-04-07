def string_encoder(input_string):
    bin_string = ' '.join(format(ord(x), 'b') for x in input_string)
    return bin_string


print(string_encoder('acuna matata'))

print(string_encoder('acuna matata')'a string'.decode('ascii')