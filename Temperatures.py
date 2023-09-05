def fun(l,x):
    c=0
    for i in l:
        c+=1
        if i>x:
            return c
    return 0


n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    if i==n-1:
        break
    s1=l[i+1:]
    s.append(fun(s1,l[i]))
s.append(0)




print(*s)
