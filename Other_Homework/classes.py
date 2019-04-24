class Person:

    # конструктор
    def __init__(self, name):
        self.name = name  # устанавливаем имя

    def display_info(self):
        print("Привет, меня зовут", self.name)


class Auto:
    def __init__(self, name):
        self.name = name

    def move(self, speed):
        print(self.name, "едет со скоростью", speed, "км/ч")


class Home:
    def __init__(self,name):
        self.name = name

    def build(self,floor):
        print(self.name, 'Home has a', floor)

    kitchen = 'Modern Kitchen'
    bathroom = 'spain board'
    walls = 'concrete'
