def pri(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    n=int(input())
    a=n-1
    b=n+1
    while True:
        if pri(n):
            print(n)
            break
        if pri(a) and pri(b):
            print(min(a,b))
            break
        if pri(a):
            print(a)
            break
        if pri(b):
            print(b)
            break
        a-=1
        b+=1