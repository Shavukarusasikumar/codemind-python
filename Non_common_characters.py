s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
a=a.replace(' ','')
b=b.replace(' ','')
x1=list(a)
x2=list(b)
c1=set(x1)
c2=set(x2)
c=0
for i in c1:
    if i.isalpha():
        if i not in c2:
            c+=1
for i in c2:
    if i.isalpha():
        if i not in c1:
            c+=1
print(c)