import json


address_book = [
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

json.dump(address_book, open("address_book", 'w'))
