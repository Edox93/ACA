i = 0
with open('damaged.jpg', 'rb') as jpg:
    with open('recover.jpg', 'wb') as new_jpg:

        while True:
            chunk = jpg.read(1024)
            i += 1
            if not chunk:
                break
            if i % 3 == 0:
                chunk = chunk[::-1]
            new_jpg.write(chunk)
