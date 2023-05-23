n=int(input())
x=list(map(int,input().split()))
a1=[]
l=[]
for i in x:
    if i in a1:
        pass
    else:
        a=x.count(i)
        a1.append(i)
        l.append(i)
        l.append(a)
print(*l)