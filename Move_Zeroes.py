n=int(input())
x=list(map(int,input().split()))
a=[]
b=[]
l=[]
for i in range(n):
    if x[i]==0:
        a.append(x[i])
    else:
        b.append(x[i])
for i in b:
    l.append(i)
for i in a:
    l.append(i)
print(*l)