n=int(input())
x=list(map(int,input().split()))
for i in range(len(x)):
    if (x[i]%2==0):
        a=i
print(a)