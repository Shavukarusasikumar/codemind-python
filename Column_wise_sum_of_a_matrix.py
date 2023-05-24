r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
for i in range(c):
    s=0
    for j in range(r):
        s+=m[j][i]
    print(s,end=' ')
        