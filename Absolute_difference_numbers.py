def pal(n):
    r=0
    while n:
        a=n%10
        r=r*10+a
        n=n//10
    return r
def whi(n,m):
    a=0
    while m:
        a=a*10+n%10
        m=m-1
        n=n//10
    return a
n,m=map(int,input().split())
x=pal(n)
s1=whi(n,m)
a1=pal(s1)
s2=whi(x,m)
print(abs(a1-s2))