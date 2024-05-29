n=int(input("enter a no. :"))
if (n>1):
     for i in range(1,int((n/2) +1)):
         if n%i!=0:
             print("not prime")
             break
         else:
             print("prime")
else:
     print("not a prime number")            
             
