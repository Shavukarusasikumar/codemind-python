n=input()
s=0
c=0
for i in n:
    if i=='R':
        s+=1
    else:
        s-=1
    if s==0:
        c+=1
print(c)