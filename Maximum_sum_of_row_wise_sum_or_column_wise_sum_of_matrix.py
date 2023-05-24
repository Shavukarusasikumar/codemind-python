r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
a=0
for i in m:
    s=sum(i)
    if s>a:
        a=s
for i in range(c):
    s1=0
    for j in range(r):
        s1+=m[j][i]
    if s1>a:
        a=s1
print(a)