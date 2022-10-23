n=int(input())
t=n
r=0
c=1
h=0
while n:
    d=n%10
    r=r*10+d
    n=n//10
#print(r)
while r:
    a=r%10
    h=h+(a**c)
    r=r//10
    c+=1
#print(h)
if t==h:
    print('True')
else:
    print('False')
