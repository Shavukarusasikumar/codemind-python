def fun(a):
    a1='[{('
    a2=']})'
    l=[]
    for i in range(len(a)):
        if a[i] in a1:
            l.append(a[i])
        else:
            if a1.index(l[-1])==a2.index(a[i]):
                l.pop()
            else:
                return i+1
    if len(l)!=0:
        return len(a)+1
    return 0
n=input()
print(fun(n))