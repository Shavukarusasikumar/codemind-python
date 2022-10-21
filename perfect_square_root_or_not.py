n=int(input())
a=n/2
i=1
b=1
while i<=a:
    if i*i==n:
        b=i*i
        break
    else:
        i=i+1
if(b==n):
    print('True')
else:
    print('False')
