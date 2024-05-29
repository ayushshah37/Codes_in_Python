def encDec(word, key):
    result = []
    for i in range(len(word)):
        res = (ord(word[i]) - 65) ^ (ord(key[i % len(key)]) - 65)  # Using modulo to repeat the key if it's shorter
        if res > 25:
            res %= 26
        result.append(chr((res) + 65))
    return ''.join(result)

original_word = 'RAMSWARUPK'
key = 'RANCHOBABA'

encrypted_result = encDec(original_word, key)
print(f'Encrypted: {encrypted_result}')
print(f'Decrypted: {encDec(word=encrypted_result, key=key)}')
