for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    c=[]
    while True:
        if len(x)==1:
            c.append(x[0])
            break
        else:
            c.append(x[-1])
            c.append(x[0])
            x.pop(-1)
            x.pop(0)
        if len(x)==0:
            break
    print(*c)