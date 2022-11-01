n=int(input())
a=[]
x=list(map(int,input().split()))
for i in x:
    a.append(i)
b=sum(a)
c=b/n
print("{0:.2f}".format(c))