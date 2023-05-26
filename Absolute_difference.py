def pri(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
x=list(map(int,input().split()))
a,b=1,1
for i in x:
    if pri(i):
        a*=i
    else:
        b*=i
print(abs(a-b))