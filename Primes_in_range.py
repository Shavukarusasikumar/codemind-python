def fun(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if fun(i):
        c+=1
print(c)