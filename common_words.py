s1=input()
a1=s1.lower()
s2=input()
a2=s2.lower()
a=a1.split()
b=a2.split()
for i in b:
    if i in a:
        print(i,end=' ')