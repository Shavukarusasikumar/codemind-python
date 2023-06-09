def fac(n):
    s=[]
    for i in range(1,n+1):
        if n%i==0:
            s.append(i)
    return sum(s)
a=input()
z=a.split(',')
x=[int(i) for i in z]
x.sort()
c=[]
for i in x:
    if fac(i) in x:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(*c)