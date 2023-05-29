s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
s1=s1.replace(' ','')
s2=s2.replace(' ','')
a=set(s1)
b=set(s2)
c=[]
if len(a)<len(b):
    a,b=b,a
for i in a:
    if i in b:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(''.join(sorted(c)))