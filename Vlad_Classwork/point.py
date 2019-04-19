import math


class Point:

    __slots__ = 'x', 'y'

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __add__(self, right):
        return self.add(right)


class Line:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        return math.sqrt(
            (self.end.x - self.start.x) ** 2 +
            (self.end.y - self.start.y) ** 2)


loong = Line(Point(3, 4), Point(5, 6))
print(loong.length())
