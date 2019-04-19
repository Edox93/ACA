class Printer:
    def __init__(self, output_path):
        # store something useful
        self.output_path = output_path

    def print(self, data):
        # print braille codes into output file
        for line in range(3):
            for symbol in data:
                print(*symbol.code[line], sep='', end=' ')
            print(' ')

    def print_line(self, line):
        pass
