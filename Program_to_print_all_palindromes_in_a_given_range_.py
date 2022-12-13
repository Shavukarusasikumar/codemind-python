def palin(n):
    r=0
    while n:
        a=n%10
        n=n//10
        r=r*10+a
    return r
m=int(input())
n=int(input())
for i in range(m,n+1):
    if palin(i)==i:
        print(i,end=' ')