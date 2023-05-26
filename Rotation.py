for i in range(int(input())):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    c=abs(n-k)
    a=x[0:c]
    l=[]
    for i in range(c,n):
        l.append(x[i])
    for i in a:
        l.append(i)
    print(*l)