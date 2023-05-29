s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
s1=s1.replace(' ','')
s2=s2.replace(' ','')
a=set(s1)
c=0
for i in a:
    if i in s2:
        c+=1
print(c)