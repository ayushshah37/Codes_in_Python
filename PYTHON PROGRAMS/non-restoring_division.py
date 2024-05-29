def nonrestore(a, q, m, n, n_len):
    print(f"{n}\t{a}\t\t{q}")
    if n==0:
        if a[0] == '1':
            a = add(a,m)
            if len(a) > n_len:
                a = a[1:]
        return  f"Quotient : bin : {q} Deci : {int(q,2)}\n Remainder : bin : {a},deci : {int(a,2)}"
    a, q = lrs(a,q)
    print(f"{n}\t{a}\t\t{q}\t\tAfter LRS ")
    if a[0] == '1':
        print("A<0")
        a = add(a,m)
        if len(a) > n_len:
            a = a[1:]
        print(f"{n}\t{a}\t\t{q} \t\tbefore operation of Q1<- ~(Amsb)")
        q = q.replace('_','1') if a[0] == '0' else q.replace('_','0')
        
    else:
        print("A>0")
        a = add(a,complement(m))
        if len(a) > n_len:
            a = a[1:]
        print(f"{n}\t{a}\t\t{q} \t\tbefore operation of Q1<- ~(Amsb)")
        
        q = q.replace('_','1') if a[0] == '0' else q.replace('_','0')
    
    return nonrestore(a, q, m, n-1,n_len)

# enter binary in string 
def complement(a):
    res = ""
    for i in a:
        if  i == '1' :
            res += '0'
        elif i == '0':
            res += '1'
            
    res = add(res,'1')
    return res

def lrs(a,q):
    a = a[1:] +q[0]
    q = q[1:] +"_"
    return a,q

def add(a,b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    if carry != 0:
        result = '1' + result
    return result.zfill(max_len)

q = int(input("Enter Q : "))
m = int(input("Enter M : "))
# q,m = int(15), int(4)
n = len(bin(max(abs(q),abs(m)))[2:])+1

q = bin(q)[2:].zfill(n-1) if q>=0 else complement(bin(q)[3:].zfill(n-1))
m = bin(m)[2:].zfill(n) if m>=0 else complement(bin(m)[3:].zfill(n))
print(f"M = {m}, Q = {q}, A={'0'*n}")
print("Count\tA\t\tQ\t\tAny action")
print("---------------------------------------------------------------")
print(nonrestore('0'*n, q.zfill(n-1), m.zfill(n), n-1, n)) 