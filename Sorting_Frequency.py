n=int(input())
x=list(map(int,input().split()))
a=set(x)
l1=[]
l2=[]
for i in a:
    c1=x.count(i)
    l1.append(i)
    l1.append(c1)
    l2.append(c1)
l2.sort(reverse=True)
l=[]
for j in l2:
    for i in range(1,len(l1),2):
        if j==l1[i]:
            if l1[i-1] not in l:
                l.append(l1[i-1])
print(*l)