a,b=map(int,input().split())
x=list(map(int,input().split()))
s=[]
c=0
for i in range(a):
    for j in range(i,a):
        p=x[i:j+1]
        if sum(p)==b:
            c+=1
print(c)