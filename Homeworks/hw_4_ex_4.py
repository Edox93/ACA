with open("damaged.jpg", "rb") as image:
  f = image.read()
  b = bytearray(f)
  print(b[0])
