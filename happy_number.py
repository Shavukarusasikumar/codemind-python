def fun(n):
    a=str(n)
    s=0
    for i in a:
        s+=int(i)**2
    return s

n=int(input())
while True:
    n=fun(n)
    if len(str(n))==1 and (n==1 or n==7):
        print('True')
        break
    elif len(str(n))==1 and (n!=1 or n!=7):
        print('False')
        break