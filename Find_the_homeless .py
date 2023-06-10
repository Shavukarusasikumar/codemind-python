n=int(input())
l1,l2=[],[]
for _ in range(n):
    a=int(input())
    l1.append(a)
for _ in range(n):
    a=int(input())
    l2.append(a)
c=0
for i in l1:
    k=0
    for j in range(len(l2)):
        if i<=l2[j]:
            l2[j]=0
            k=1
            break
    if k==0:
        c+=1
print(c)