r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
s=0
for i in m:
    a=sum(i)
    if a>s:
        s=a
print(s)