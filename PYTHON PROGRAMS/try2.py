# def vernam(key,plaintext):
#     result=[]




# plaintext=input("enter Plaintext: ").upper()
# Key=input("Enter Key:").upper()

pt=input("enter PT:").upper()
key=int(input("ener key :"))

cipher_text=[]

for i in range(len(pt)):
    ct=chr(((ord(pt[i])+key)%65)+65)
    cipher_text.append(ct)


print(cipher_text)
    