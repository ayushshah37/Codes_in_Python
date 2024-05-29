def booth(a,m,q,q1,n,n_len):
    print(f"{n}\t{a}\t{q}\t{q1}")

    if(n==0):
        if(a[0]=='0'):
            return(f" answer is positive :{a,q},decimal:{int(a+q,2)}")
    
        else:
            return (f"answer is negative: {a, q}, 2nd complement: {complement(a+q)}\n decimal: {int(complement(a+q),2)}")
    if(q[-1]=='1' and q1[-1]=='0'):
        print("case of 1 and 0 ->")
        print("case of 0 and 1 ->")
        a=add(a,complement(m.zfill(n)))
        if(len(a)!=n_len):
            a=a[1:]
        print(f"{n}\t{a}\t{q}\t{q1}         before ans")
        a,q,q1=ars(a,q,q1)

    elif(q[-1]=='0' and q1[-1]=='1'):
        print("case of 0 and 1 ->")
        a=add(a,m)
        if(len(a)!=n_len):
            a=a[1:]
        print(f"{n}\t{a}\t{q}\t{q1}         before ans")
        a,q,q1=ars(a,q,q1)
    
    elif((q[-1]=='1' and q1[-1]=='1') or (q[-1]=='0' and q1[-1]=='1')):
        print("case of 00 or 11 ->")
        a,q,q1=ars(a,q,q1)
    return booth(a,m,q,q1,n-1,n_len)

    
def ars(a,q,q1):
    q1=q[-1]
    q=a[-1]+q[:-1]
    a=a[0]+a[:-1]
    return a,q,q1


def add(a,b):
    max_len=max(len(a),len(b))
    a=a.zfill(max_len)
    b=b.zfill(max_len)
    result=''
    carry=0
    for i in range(max_len-1,-1,-1):
        r=carry
        if(a[i]=='1'):
            r+=1
        else:
            r+=0
        if(b[i]=='1'):
            r+=1
        else:
            r+=0 
        result=('1' if (r%2==1) else '0')+result
        carry=0 if r<2 else 1
    if(carry!=0):
        result='1'+result
    return result.zfill(max_len) 

def complement(a):
    res=""
    for i in a:
        if(i=='1'):
            res=res+'0'
        elif(i=='0'):
            res=res+'1'
    res=add(res,'1')
    return res




a=int(input("enter number-1 : "))
b=int(input("enter number-2 : "))

n=len(bin(max(abs(a),abs(b)))[2:])+1

if(a>0):
    a=bin(a)[2:].zfill(n)
else:
    a=complement(bin(a)[3:].zfill(n))

if(b>0):
    b=bin(b)[2:].zfill(n)
else:
    b=complement(bin(b)[3:].zfill(n))

print(f"M={a},Q={b},Q={'0'*n},Count={n}")
print("Count\tA\tQ\tQ1")
print("---------------------------------------------------")
print(booth('0'*n,a.zfill(n),b.zfill(n),'0',n,n))

