def pal(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False
n=int(input())
a=n-1
b=n+1
while True:
    if pal(a) and pal(b):
        print(a,b)
        break
    elif pal(b):
        print(b)
        break
    elif pal(a):
        print(a)
        break
    else:
        a-=1
        b+=1