n=input()
c=0
d=0
for i in n:
    if i=='U':
        c+=1
    elif i=='D':
        c-=1
    elif i=='L':
        d+=1
    elif i=='R':
        d-=1
if c==d==0:
    print('True')
else:
    print('False')