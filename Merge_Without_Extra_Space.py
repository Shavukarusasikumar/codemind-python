for _ in range(int(input())):
    a,b=map(int,input().split())
    x1=list(map(int,input().split()))
    x2=list(map(int,input().split()))
    c=x1+x2
    c.sort()
    for i in range(a):
        x1[i]=c[i]
    for i in range(b):
        x2[i]=c[i+a-1]
    print(*c)
    
