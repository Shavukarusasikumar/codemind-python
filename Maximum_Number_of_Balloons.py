n=input()
n=n.lower()
n=n.replace(' ','')
a=list(n)
l=[]
c='banlo'
for i in c:
    l.append(a.count(i))
l[-1]=l[-1]//2
l[-2]=l[-2]//2
print(min(l))

    