n=input()
n=n.lower()
n=n.replace(' ','')
a=list(n)
l=[]
for i in a:
    if a.count(i)==1:
        l.append(i)
        print(i)
        break
if len(l)==0:
    print(-1)