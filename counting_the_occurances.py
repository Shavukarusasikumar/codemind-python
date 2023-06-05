n=input()
a=input()
n=n.lower()
n=n.replace(' ','')
c=n.count(a)
if c==0:
    print(-1)
else:
    print(c)