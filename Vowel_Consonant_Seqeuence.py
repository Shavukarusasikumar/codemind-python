n=input()
a=list(n)
l=[]
l1,l2=[],[]
s=''
for i in a:
    if i in 'aeiou':
        l1.append(i)
        if len(l2)!=0:
            s+='C'
            l2=[]
    else:
        l2.append(i)
        if len(l1)!=0:
            s+='V'
            l1=[]
if len(l1)!=0:
    s+='V'
if len(l2)!=0:
    s+='C'
print(s)