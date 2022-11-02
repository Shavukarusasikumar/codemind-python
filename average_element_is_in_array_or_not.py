n=int(input())
sum=0
x=list(map(int,input().split()))
for i in range(len(x)):
    sum=sum+x[i]
a=sum//n
if a in x:
    print('True')
else:
    print('False')