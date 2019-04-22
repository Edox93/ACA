import copy


class A:
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")

    someNumber = 10


someObject = A()
print(someObject.someNumber)

copy.copy(someObject)
copy.deepcopy(someObject)
