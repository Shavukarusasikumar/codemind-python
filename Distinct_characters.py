n=input()
n=n.lower()
n=n.replace(' ','')
a=list(n)
b=set(a)
c=list(b)
d=sorted(c)
print(''.join(d))