def prime(n):
    a=0
    for n in range(2,n):
        if n%i==0:
            a+=1
    if a==0:
        return 1
    return 0
n=int(input())
a=0
for i in range(2,n):
    for j in range(2,n):
      if i*j==n and prime(i)==1 and prime(j)==1:
          s1=j
          s2=i
          a+=1
if a==1:
    print(s1,s2)
else:
    print(-1)
         
