def pri(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        return 1
    return 0
n=int(input())
l=[]
for i in range(2,n):
    for j in range(2,n):
        if pri(i)==1 and pri(j)==1:
            if i*j==n:
                l.append(i)
                l.append(j)
if sum(l)==0:
    print(-1)
else:
    l=set(l)
    for i in l:
        print(i,end=' ')