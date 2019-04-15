with open("damaged.jpg", "rb") as image:
    with open('recovered.jpg', 'wb') as recovered_file:
        chunk_count = 0
        while True:
            chunk = image.read(1024)
            chunk_count += 1
            if not chunk:
                break
            if chunk_count % 3 == 0 and chunk_count != 0:
                chunk = bytearray(chunk[::-1])
            recovered_file.write(bytearray(chunk))

