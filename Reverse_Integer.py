n=int(input())
r=0
if n>0:
    while n:
        p=n%10
        r=r*10+p
        n=n//10
    print(r)
else:
    n=-n
    while n:
        p=n%10
        r=r*10+p
        n=n//10
    print(-r)