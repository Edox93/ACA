wars = {1945: 1, 2018: 20}

print(wars)

cities = {(40.10, 44.30): 'Yerevan',
          (41.50, 87.41): 'Chicago'}

yerevan_coord = list(cities.keys())[0]

yerevan_coord[0] = 45.10

coord = (40.10, 44.34)

print(cities.get(coord, 'Unkown place'))
