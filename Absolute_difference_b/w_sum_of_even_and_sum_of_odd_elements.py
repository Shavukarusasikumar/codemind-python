n=int(input())
e=[]
o=[]
x=list(map(int,input().split()))
for i in x:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
a=sum(e)
b=sum(o)
if a>=b:
    print(a-b)
else:
    print(b-a)