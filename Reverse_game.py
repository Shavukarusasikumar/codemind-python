n=int(input())
x=list(map(int,input().split()))
l=[]
for i in x:
    i=str(i)
    l.append(int(i[::-1]))
print(*l)