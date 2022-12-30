def pri(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        return 1
    return 0
n=int(input())
x=list(map(int,input().split()))
k=int(input())
a=0
for i in x:
    if pri(i)==1 and i>=k:
        a+=1
print(a)