n=int(input())
x=list(map(int,input().split()))
l1,l2=[],[]
for i in x:
    if i%2!=0:
        l1.append(i)
    else:
        l2.append(i)
i=len(l1)
j=len(l2)
c=[]
while True:
    if len(l1)==len(l2)==0:
        break
    elif len(l1)==0:
        c.append(l2[0])
        l2.pop(0)
    elif len(l2)==0:
        c.append(l1[0])
        l1.pop(0)
    else:
        c.append(l1[0])
        c.append(l2[0])
        l1.pop(0)
        l2.pop(0)
if len(c)%2!=0:
    c.append(0)
    print(*c)
else:
    print(*c)        