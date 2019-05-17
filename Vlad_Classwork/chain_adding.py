class add(int):

    def __call__(self, n: int) -> int:
        return add(self + n)


class add:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return add(self.value + other)

    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':
    print(add(1)(2)(3)(4))  # 10
    print(add(5))  # 5
    print(add(5) == 5)  # True
