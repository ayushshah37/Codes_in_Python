
word='AYUSHSHAH'
key="HELLO"
for i in range(len(word)):
    res = (ord(word[i]) - 65) ^ (ord(key[i % len(key)]) - 65)
    print(res,chr(res))

    if res > 25:
            res %= 26
    result.append(chr((res) + 65))
    ''.join(result)
print(result)
