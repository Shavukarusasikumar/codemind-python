n=int(input())
r=0
rev=0
sn=n*n
while n:
    d=n%10
    n=n//10
    r=r*10+d
sr=r*r
while sr:
    a=sr%10
    sr=sr//10
    rev=rev*10+a
if(rev==sn):
    print('True')
else:
    print('False')
