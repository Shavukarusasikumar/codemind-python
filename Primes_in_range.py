def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n1=int(input())
n2=int(input())
c=0
for n in range(n1,n2+1):
    if (prime(n) and n!=1):
        c+=1
print(c)