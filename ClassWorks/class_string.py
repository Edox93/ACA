class String:

    def __init__(self, value: str):
        self.value = str(value)

    def __getitem__(self, key: int) -> str:
       return self.value[key]

    def __setitem__(self, key: int, value: str):
        data = list(self.value)
        data[key] = value
        self.value = ''.join(value)
        self.value = f"{self.value[:key]}{value}{self.value[key + 1:]}"

    def __len__(self) -> int:
        return  len(self.value)

    def __add__(self, other):
        pass

    def upper(self):
        self.value = self.value.upper()
        # self.value = list(''.join(self.value).upper())
        self.value = map(str.upper, self.value)



    def to_int(self, default: int = None):
        try:
            return int(self.value)
        except:
            return default

    def to_float(self, default: float = None):
        try:
            return
        except:
            return default





if __name__ == "__main__":
    txt = String('some thing')
    print(txt)
    print(len(txt))
    print(txt[2])
    txt[2] = 'l'
    print(txt[2])
    print(len(txt))
    print(txt.to_int(0))
