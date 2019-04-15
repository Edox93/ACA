import binascii


def string_encoder(input_string: str) -> str:
    bin_string = bin(int.from_bytes(input_string.encode(), 'big')).lstrip('0b')
    return bin_string


def string_decoder(input_string: str) -> str:
    bin_start = '0b'
    full_string = bin_start + input_string
    print(full_string)
    bin_string = int(full_string, 2)
    return bin_string.to_bytes((bin_string.bit_length() + 7) // 8, 'big').decode()


if __name__ == '__main__':
    user_input = input('please input your string for decoding to binary: ')
    print(string_encoder(user_input))
    user_input2 = input('please input your binary string for decoding: ')
    print(string_decoder(user_input2))
