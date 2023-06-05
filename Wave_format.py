n = int(input())
x1 = list(map(int,input().split()))
x=sorted(x1,reverse=True)
l=[]
while True:
    if len(x)==0:
        break
    if len(x)==1:
        l.append(x[0])
        break
    l.append(x[1])
    l.append(x[0])
    x.pop(1)
    x.pop(0)
print(*l)