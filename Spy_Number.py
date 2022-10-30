n=int(input())
a=0
b=1
while n:
    d=n%10
    a=a+d
    b=b*d
    n=n//10
if(a==b):
    print("Spy Number")
else:
    print('Not Spy Number')
