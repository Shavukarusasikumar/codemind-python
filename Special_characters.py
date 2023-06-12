n=input()
c=0
l1,l2=[],[]
for i in n:
    if not i.isalpha() and not i.isdigit():
        c+=1
    if i.isdigit():
        if int(i)%2==0:
            l1.append(i)
        else:
            l2.append(i)
k=[]
if c%2==0:
    while True:
        if len(l1)==len(l2)==0:
            break
        if len(l1)==0:
            k.append(l2.pop(0))
        elif len(l2)==0:
            k.append(l1.pop(0))
        else:
            k.append(l1.pop(0))
            k.append(l2.pop(0))
else:
    while True:
        if len(l1)==len(l2)==0:
            break
        if len(l1)==0:
            k.append(l2.pop(0))
        elif len(l2)==0:
            k.append(l1.pop(0))
        else:
            k.append(l2.pop(0))
            k.append(l1.pop(0))
print(''.join(k))
    