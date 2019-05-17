class MySet:
    def __init__(self):
        self.data = []
        self.uniques = set()

    def add(self, value):
        if value not in self.uniques:
            self.data.append(value)
            self.uniques.add(value)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def __repr__(self):
        return str(self.data)

if __name__ == '__main__':
    data = MySet()
    data.add(1)
    data.add(2)
    data.add(1)
    print(data)
    print(len(data))
    print(data[1])
