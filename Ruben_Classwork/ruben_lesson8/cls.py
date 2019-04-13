import hashlib


class User:
    def __init__(self, username='', password=''):
        self.username = username
        self.set_password(password)

    def change_username(self, new_username):
        self.username = new_username

    def set_password(self, password):
        self.__password = hashlib.sha256(password.encode()).hexdigest()

    def get_password(self):
        return self.__password

    def __repr__(self):
        return f'User instance - {self.username}'

    def __hash__(self):
        print('my hash')
        data = f'{self.username}{self.__password}'
        return hash(hashlib.sha256(data.encode()).hexdigest())

    def __lt__(self, other):
        return len(self.username) < len(other.username)


users = [User('garo777', 'asdfadsf'), User('garo8', 'asdfadsf')]

print(sorted(users))
