r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
c=0
for i in m:
    if sorted(i)==i or sorted(i,reverse=True)==i:
        c+=1
print(c)
