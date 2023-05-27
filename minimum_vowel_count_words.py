n=input()
a=n.split()
v='aeiou'
l=[]
for i in a:
    c=0
    for j in i:
        if j in v:
            c+=1
    l.append(c)
x=min(l)
print(l.count(x))