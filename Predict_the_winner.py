n=int(input())
x=list(map(int,input().split()))
c=n//2
a,b=0,0
for i in range(0,c):
    a+=x[i]
for i in range(c,n):
    b+=x[i]
d=abs(a-b)
if d%4==0:
    print('X')
else:
    print('Y')