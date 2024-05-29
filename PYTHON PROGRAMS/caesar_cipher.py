def encrypt(text,key):
    result = ""
    for char in text:
        base = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char)-base + key)%26+base) if (char.isupper()) else chr((ord(char)-base + key)%26+base)
    return result
def decrypt(text,key):
    result = ""
    for char in text:
        base = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - base - key) % 26 + base)
    return result
text = "ATTACKAToNCEY"
key = 3
cipherText=encrypt(text,key)
print (f"Text:{text}\nShift:{s}\nCipher:{cipherText}\nDecrypted:{decrypt(cipherText,key)}")