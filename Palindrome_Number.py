def pal(n):
    r=0
    while n:
        a=n%10
        r=r*10+a
        n=n//10
    return r
a=int(input())
for i in range(a):
    s=int(input())
    if pal(s)==s:
        print("True")
    else:
        print("False")
    