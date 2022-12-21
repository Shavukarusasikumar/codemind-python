def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        return 1
    return 0
a=int(input())
b=int(input())
c=a+b+1
d=0
while c:
    d+=1
    if prime(c)==1:
        break
    else:
        c=c+1
print(d)