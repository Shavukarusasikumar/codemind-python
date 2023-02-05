def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        return 1
    return 0
t=int(input())
for i in range(1,t+1):
    n=int(input())
    if prime(n)==1:
        print(n)
    else:
        h=n
        l=n
        while True:
            h+=1
            l=l-1
            if prime(l)==1:
                print(l)
                break
            if prime(h)==1:
                print(h)
                break
            
        