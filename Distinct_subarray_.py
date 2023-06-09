a=int(input())
b=int(input())
x=[i for i in range(a,b+1)]
s=[]
c=0
for i in range(len(x)):
    for j in range(i,len(x)):
        p=x[i:j+1]
        if sum(p)%2!=0:
            c+=1
print(c)