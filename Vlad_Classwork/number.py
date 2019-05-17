""" Implement a class which will represent a number """
class Number(int):

    def __getitem__(self, index):
        return str(self)[index]

    def __len__(self):
        return len(str(self))


if __name__ == '__main__':
    num = Number(421)
    print(num[1])
