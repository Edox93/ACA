import sqlite3


conn = sqlite3.connect('listam.db')

cur = conn.cursor()

cur.execute('CREATE TABLE users ('
            'id INTEGER PRIMARY KEY,'
            'name CHAR(150))')

cur.execute('CREATE TABLE contacts ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'user_id INTEGER,'
            'phone TEXT,'
            'FOREIGN KEY(user_id) REFERENCES users(id)'
            ')')

cur.execute('CREATE TABLE posts ('
            'id INTEGER PRIMARY KEY,'
            'user_id INTEGER,'
            'title TEXT,'
            'descr TEXT,'
            'FOREIGN KEY(user_id) REFERENCES users(id)'
            ')')
