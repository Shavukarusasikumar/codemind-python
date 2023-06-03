a=input()
b=input()
c=a+b
c1=[]
for i in c:
    if i.isalpha():
        c1.append(i)
print(''.join(sorted(c1)))