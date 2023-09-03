from itertools import permutations
n,k=map(int,input().split())
li=[i for i in range(1,n+1)]
c=list(permutations(li,n))
x=c[k-1]
z=''
for i in x:
    z+=str(i)
print(z)