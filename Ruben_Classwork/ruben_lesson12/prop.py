class User:
    def __init__(self):
        self._username = ''

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, name):
        self._username = name.upper()

    def __call__(self):
        return "Username: {}".format(self._username)

    # username = property(get_username, set_username)


admin = User()

# admin.set_username('garo777')
# print(admin.get_username())

admin.username = 'garik777'
print(admin.username)

print(admin())
