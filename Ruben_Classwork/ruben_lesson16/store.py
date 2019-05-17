import sqlite3


conn = sqlite3.connect('example.db')

cur = conn.cursor()

"""
cur.execute('CREATE TABLE items ('
            'code TEXT,'
            'name TEXT,'
            'price REAL,'
            'count INTEGER)')

cur.execute('INSERT INTO items VALUES '
            '("AVO", "Avocado", 1500.0, 10)')

conn.commit()
"""

cur.execute('SELECT name, price FROM items WHERE code="AVO"')

for item in cur:
    print(item)
