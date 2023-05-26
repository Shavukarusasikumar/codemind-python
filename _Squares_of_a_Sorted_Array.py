n=int(input())
x=list(map(int,input().split()))
l=[]
for i in x:
    i=abs(i)
    l.append(i**2)
a=sorted(l)
print(*a)