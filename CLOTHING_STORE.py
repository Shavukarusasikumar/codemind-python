n = int(input())
x = list(map(int,input().split()))
d={}
c=0
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    c+=d[i]//2
print(c)