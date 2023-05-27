n=input()
a=n.split()
v="aeiou"
l=[]
c1=0
for i in a:
    c=0
    i=i.lower()
    for j in i:
        if j in v:
            c+=1
    l.append(c)
m=max(l)
for i in a:
    c=0
    i=i.lower()
    for j in i:
        if j in v:
            c+=1
    if c==m:
        c1+=1
print(c1)
            