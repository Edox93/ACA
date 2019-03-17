while True:
    binstr = input()

    ok = True
    for ch in binstr:
        if ch != '0' and ch != '1':
            ok = False
            break

    if not ok:
        print('{ERROR}')
        continue:

    if len(binstr.replace('0', '1')).replace('1', '0')) !=
        print('{ERROR}')
        continue

print()