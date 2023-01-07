def pal(n):
    r=0
    while n:
        a=n%10
        r=r*10+a
        n=n//10
    return r
n,k=map(int,input().split())
n1=pal(n)
a=n%(10**k)
b=n1%(10**k)
c=pal(b)
print(abs(a-c))