import binascii


def string_encoder(input_string: str) -> str:
    bin_string = ''.join(format(ord(x), 'b') for x in input_string)
    return bin_string


encoded_string = string_encoder('h')
print(encoded_string)


encoded_string = int(encoded_string, 2)
decoded_to_ascii = binascii.hexlify(encoded_string)

print(decoded_to_ascii)

a = decoded_to_ascii.decode('utf-8')
print(a)

ob


