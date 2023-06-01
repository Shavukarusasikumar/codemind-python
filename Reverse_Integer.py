def pal(n):
    n=str(n)
    return int(n[::-1])
n=int(input())
if n<0:
    a=abs(n)
    c=str(pal(a))
    s='-'+c
    print(int(s))
else:
    print(pal(n))