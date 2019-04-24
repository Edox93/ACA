class Person:
    __name = ''
    hobby = ''
    dob = int

    def info(self):
        return self.__name, self.hobby, self.dob


class AnotherPerson:
    def __init__(self, name):
        self.name = name
        name = 'Aram'
        print("Constructor", name)

    def __del__(self):
        name = 'Aram'
        print("Destructor", name)


# Edgar = Person()
# Edgar.name = 'Edgar.Ramazyan'
# Edgar.hobby = 'MMA'
# Edgar.dob = 26
#
# print(type(Edgar.info()))
# print(Edgar.info())
# print(Person)
# print(type(Person))

Arman = AnotherPerson('ala')
Arman.name = 'Levon'
Arman = AnotherPerson('xss')



