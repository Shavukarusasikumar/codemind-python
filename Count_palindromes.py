def palin(n):
    r=0
    while n:
        a=n%10
        n=n//10
        r=r*10+a
    return r
l=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if palin(i)==i:
        c+=1
print(c)