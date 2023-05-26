n=int(input())
x=list(map(int,input().split()))
k=int(input())
a=max(x)
l=[]
for i in x:
    if i+k>=a:
        l.append('True')
    else:
        l.append('False')
print(*l)