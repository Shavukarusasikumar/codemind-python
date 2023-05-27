def fun(n):
    a=list(n)
    l=[]
    for i in range(len(a)):
        if a[i].isalnum():
            l.append(a[i])
            a[i]='#'
    l.sort()
    for i in range(len(a)):
        if a[i]=='#':
            a[i]=l[0]
            l.pop(0)
    return a
n=input()
x=n.split()
for i in x:
    z=fun(i)
    print(''.join(z),end=' ')
    