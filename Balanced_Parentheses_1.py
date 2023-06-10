def fun(n):
    a1='[{('
    a2=']})'
    l=[]
    for i in n:
        if i in a1:
            l.append(i)
        else:
            if a1.index(l[-1])==a2.index(i):
                l.pop()
            else:
                return 'False'
    return 'True'
n=input()
print(fun(n))