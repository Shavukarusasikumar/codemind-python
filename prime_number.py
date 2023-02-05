def pri(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        return 1
    return 0
n=int(input())
if pri(n)==1:
    print('prime')
else:
    print('not a prime')