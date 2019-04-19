from functools import reduce


class Array:

    def __init__(self, data: list):
        self.data = data

    def delete_nth(self, count: int) -> list:
        result = []
        for item in self.data:
            if result.count(item) < count:
                result.append(item)
        return result


def delete_nth(order, max_e):
    return reduce(lambda x, y: x + [y] if x.count(y) < max_e else x, order, [])


if __name__ == '__main__':
    print(delete_nth([1, 2, 3, 1, 2, 8, 9, 1, 3, 1, 3, 12, 5], 2))    

    obj = Array([1, 2, 3, 1, 2, 8, 9, 1, 3, 1, 3, 12, 5])
    print(obj.delete_nth(2))
    print(obj.delete_nth(3))
