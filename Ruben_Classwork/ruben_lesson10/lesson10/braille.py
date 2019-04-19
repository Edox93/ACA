from console import ConsoleReader
from translator import Translator
from printer import Printer


if __name__ == '__main__':
    reader = ConsoleReader()

    args = reader.get_args()

    # read data form args.data_path file
    with open(args.data_path) as data_file:
        data = data_file.read().strip()

    translator = Translator(data, args.alphabet_path)
    translator.translate()

    printer = Printer(args.output_path)
    printer.print(translator.get_translation())
