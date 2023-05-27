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
x=list(n)
z=fun(x)
print(''.join(z))
    