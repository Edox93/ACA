# import json
import pickle


# data = json.load(open('address_book'))

"""
data = [
    {
        "first_name": "Garegin",
        "last_name": "Makunc",
        "langs": ('en', 'am', 'kz')
    },
    {
        "first_name": "Martun",
        "last_name": "Karagozyan",
        "langs": ('am', 'ru', 'fr')
    }
]
"""

data = []

data.append(input())
data.append(input())
data.append(input())
data.append(input())

pickle.dump(data, open('address_book_pckl', 'wb'))
