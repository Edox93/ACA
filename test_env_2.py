import argparse


def recover():
    with open('damaged.jpg', 'rb') as jpg:
        i = 0
        new_array = bytearray()

        while True:
            chunk = jpg.read(1024)
            i += 1
            if not chunk:
                break
            if i % 3 == 0 and i != 0:
                chunk = bytearray(chunk[::-1])
            new_array += bytearray(chunk)

    with open('damaged.jpg', 'wb') as new:
        new.write(new_array)


def recover_as():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--input_filename', type=str, help='Input recovery filename', required=True)
    new_file_name = parser.parse_args().input_filename

    i = 0
    with open('damaged.jpg', 'rb') as jpg:
        with open(f'{new_file_name}.jpg', 'wb') as new_jpg:

            while True:
                chunk = jpg.read(1024)
                i += 1
                if not chunk:
                    break
                if i % 3 == 0 and i != 0:
                    chunk = bytearray(chunk[::-1])
                new_jpg.write(bytearray(chunk))
