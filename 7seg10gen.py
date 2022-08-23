with open('./7seg10u.bin', 'wb+') as output:
    for i in range(255):
        output.write(int(str(i), base=16).to_bytes(2, byteorder = 'little'))