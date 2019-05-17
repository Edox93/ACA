import os

print(os.walk('.'))


with open('iterators.py') as source:
    file_iter = iter(source)
    print(next(file_iter))
    # for line in source:
    #    pass  # print(line.strip())
