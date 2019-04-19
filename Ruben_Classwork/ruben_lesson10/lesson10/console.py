from argparse import ArgumentParser


class ConsoleReader:
    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument('data_path')
        self.parser.add_argument('alphabet_path')
        self.parser.add_argument('output_path')

        self.arguments = self.parser.parse_args()

    def get_args(self):
        return self.arguments
