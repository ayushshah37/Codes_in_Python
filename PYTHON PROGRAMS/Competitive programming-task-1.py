a,b=input("enter 2 values:").split()
print("nr:",a)
print("dr:",b)
print()
#a+=1
a=int(a)
b=int(b)
#b+=1
#print (type(a))
#print(b)
c=0
#c+=1
#print(c)

while (a%b!=0):
     a+=1
     c+=1
print(c)