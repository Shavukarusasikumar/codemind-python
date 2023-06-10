n=input()
k=int(input())
a1=k//(len(n)-1)
a2=k%(len(n)-1)
c1=(n.count('a'))*a1
z=n[:a2]
c2=z.count('a')
print(c1+c2)
