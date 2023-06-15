def fun(n):
    a=n.split(':')
    c=0
    k=len(a[0])
    for i in n:
        if i.isdigit() and int(i)<=k:
            if int(i)>c:
                c=int(i)
    if c==0:
        return 'X'
    return a[0][c-1]
n=input()
a=n.split(',')
s=''
for i in a:
    s+=fun(i)
print(s)
