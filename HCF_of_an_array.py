import math
n=int(input())
x=list(map(int,input().split()))
a=x[0]
for i in range(1,n):
    a=math.gcd(a,x[i])
print(a)