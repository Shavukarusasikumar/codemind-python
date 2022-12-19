n=int(input())
x=list(map(int,input().split()))
b=0
for i in x:
    a=x.count(i)
    if a>b and a>n/2:
        c=i
print(c)