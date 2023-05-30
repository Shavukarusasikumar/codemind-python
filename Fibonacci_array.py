def fib(x):
    a=x[0]
    b=x[1]
    for i in range(2,len(x)):
        if x[i]==(a+b):
            a=b
            b=x[i]
        else:
            return False
    return True

n=int(input())
x=list(map(int,input().split()))
if len(x)<=2:
    print('no')
elif fib(x):
    print('yes')
else:
    print('no')