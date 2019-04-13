names, dups = {}, {}
with open('names.txt', 'r') as source:
    with open('dest.txt', 'w') as dest:
        for name in source:
            if name in names and name not in dups:
                dest.write(f'name\n')
                dups.add(name)
            names.add(name)
