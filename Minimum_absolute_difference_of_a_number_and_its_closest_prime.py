def pri(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
a=n-1
b=n+1
if pri(n):
    print(0)
else:
    while True:
        if pri(a):
            c=a
            break
        elif pri(b):
            c=b
            break
        else:
            a-=1
            b+=1
    print(abs(c-n))