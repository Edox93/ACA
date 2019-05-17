class User:
    _obj = None

    def __new__(cls):
        if User._obj is None:
            User._obj = super().__new__(cls)

        return User._obj


user = User()
print(user)
user = User()
print(user)
user = User()
print(user)
user = User()
print(user)
