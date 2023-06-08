n=input()
l=[]
for i in n:
    if i.isdigit():
        l.append(i)
c=100
a=set(l)
l=list(a)
l.sort(reverse=True)
c=100
for i in range(len(l)-1,-1,-1):
    if int(l[i])%2==0:
        c=l.pop(i)
        break
    
if c==100:
    print(-1)
else:
    l.append(c)
    print(int(''.join(l)))