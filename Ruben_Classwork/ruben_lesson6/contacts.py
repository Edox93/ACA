import json


my_contacts = json.load(open('address_book'))

print(my_contacts[0]['first_name'])

print(type(my_contacts[0]['langs']))
