n=int(input())
n1=0
n2=1
c=0
b=0
while c<n:
    print(n1,end=" ")
    nth=n1+n2
    n1=n2
    n2=nth
    c+=1