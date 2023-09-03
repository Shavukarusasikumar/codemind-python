for _ in range(int(input())):
    a,b=map(int,input().split())
    i=0
    c=
    l=[]
    z=0
    while True:
        if (i*i)%b==a:
            print(i)
            break
        c-=1
        if c==0:
            z=1
            break
        i+=1
    if c==0 and z==1:
        print(-1)
    