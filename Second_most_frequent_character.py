n=input()
c=[]
c1=[]
for i in n:
    if i not in c:
        v=n.count(i)
        c.append(v)
        c.append(i)
        c1.append(v)
c1=set(c1)
c1=list(c1)
c1.sort()
if c1.count(c1[0])==len(c1):
    print(-1)
else:
    k=c1[-2]
    for i in range(0,len(c),2):
        if c[i]==k:
            print(c[i+1])
            break


    
