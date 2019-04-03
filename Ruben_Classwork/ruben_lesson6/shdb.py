import shelve


"""
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
birth_date = input('Enter birth date: ')


with shelve.open('my.db') as db:
    db[f'person_{len(list(db.keys()))}'] = {
        'fn': first_name, 'ln': last_name, 'bd': birth_date
    }

"""

with shelve.open('my.db') as db:
    for k, v in db.items():
        print(k, '-', v)
