import json

employees = json.load(open('employee'))

employees['employees'][0]['lastName'] = 'Makunc'

json.dump(employees, open('employee', 'w'))
