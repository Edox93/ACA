arr = [1,2,3,4,5]
for item in arr:
    print(item)

for idx in range(len(arr)):
    print(idx, '-', arr[idx])

for idx, item in enumerate(arr):
    print(idx, '-', arr[idx])

text = ''
for char in text:
    print(char)

for idx in range(len(text)):

    print(idx,'-', text[idx])


dt = ('a':1, 'b':2, 'c':3)
for key in dt:
    print(key, '-', dt[key])


