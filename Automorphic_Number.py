n=int(input())
if n<0:
    n=n*(-1)
s=n*n #s quare of the given num
l=len(str(n)) # to get the length of the num
k=s%(10**l)
if k==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
