r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
a=0
for i in range(c):
    s=0
    for j in range(r):
        s+=m[j][i]
    if s>a:
        a=s
print(a)