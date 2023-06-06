n=int(input())
x=list(map(int,input().split()))
l1,l2=[],[]
for i in x:
    if i==1:
        l1.append(i)
    else:
        l2.append(i)
l=l2+l1
print(*l)