n=int(input())
x=list(map(int,input().split()))
l=[]
for i in range(0,n,2):
    for j in range(x[i]):
        l.append(x[i+1])
print(*l)