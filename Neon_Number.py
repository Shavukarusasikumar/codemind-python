n=int(input())
a=n*n
b=str(a)
k=0
for i in b:
    k+=int(i)
if k==n:
    print('Neon Number')
else:
    print("Not Neon Number")