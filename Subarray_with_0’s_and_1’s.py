n=int(input())
x=list(map(int,input().split()))
s=[]
c=0
a1=0
a2=0
for i in range(n):
    for j in range(i,n):
        p=x[i:j+1]
        if p.count(1)==p.count(0):
            if len(p)>c:
                c=len(p)
                a1=i
                a2=j
if a1==0 and a2==0:
    print(-1)
else:
    print(a1,a2)