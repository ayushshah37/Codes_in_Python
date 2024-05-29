a=int(input("enter number of terms:"))
f=0
s=1
if a<=0:
     print("the requested series is",f)
else :
     print(f,s,end="")
     for x in range(2,a):
      next =f+s
     print(next,end="")
     f=s
     s=next