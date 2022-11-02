n=int(input())
x=list(map(int,input().split()))
z=int(input())
c=0
for i in x:
    if i==z:
        c+=1
print(c)