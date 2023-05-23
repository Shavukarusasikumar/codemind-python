r,c=map(int,input().split())
x=[]
a1=0
for i in range(r):
    a=list(map(int,input().split()))
    x.append(a)
    a1+=sum(a)
print(a1)
