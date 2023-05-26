n=int(input())
x=list(map(str,input().split()))
c=0
for i in x:
    if len(i)%2==0:
        c+=1
print(c)