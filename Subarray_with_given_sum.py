for _ in range(int(input())):
    n,s=map(int,input().split())
    l=list(map(int,input().split()))
    f1,f2=False,False
    for i in range(n):
        for j in range(n):
            if sum(l[i:j+1])==s:
                f1=True
                f2=True
                print(i+1,j+1)
                break
        if f1:
            break
    if not f2:
        print(-1)