r,c=map(int,input().split())
m1=[list(map(int,input().split())) for i in range(r)]
for i in m1:
    print(sum(i),end=' ')
