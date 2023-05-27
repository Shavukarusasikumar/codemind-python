n=input()
n=n.lower()
a=n.split()
l=[]
for i in a:
    l.append(set(i))
b=l[0]
for i in range(len(l)):
    b=b.intersection(l[i])
z=list(b)
if len(z)==0:
    print(-1)
else:
    print(min(z))

