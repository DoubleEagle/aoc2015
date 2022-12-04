import hashlib

input = "ckczppom"

i = 310000000

while True:
    if i % 10000000 == 0:
        print(i)
    to_hash = input + str(i)
    res = hashlib.md5(bytes(to_hash, 'utf-8')).hexdigest()
    if res[:5] == "000000":
        print(i, to_hash)
        exit()
    i += 1