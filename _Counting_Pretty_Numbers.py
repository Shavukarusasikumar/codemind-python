x=int(input())
for i in range(x):
    m,n=map(int,input().split())
    c=0
    for i in range(m,n+1):
        a=i%10
        if a==2 or a==3 or a==9:
            c+=1
    print(c)