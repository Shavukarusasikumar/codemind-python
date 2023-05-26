s1=input()
s2=input()
s3 = s1.lower()
s4 = s2.lower()
m1 = list(s3)
m2 = list(s4)
m3,m4 = [],[]
for i in m1:
    if i.isalpha():
        m3.append(i)
for i in m2:
    if i.isalpha():
        m4.append(i)
l = [] 
m5=set(m3)
m6=set(m4)
for i in m5:
    if i not in m6:
        l.append(i)
for i in m6:
    if i not in m5:
        l.append(i)
c = sorted(l)
d = ''.join(c)
print(d)