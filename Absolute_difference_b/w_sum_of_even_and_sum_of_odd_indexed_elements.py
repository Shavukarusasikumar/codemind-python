n=int(input())
e=[]
o=[]
x=list(map(int,input().split()))
for i in range(len(x)):
    if i%2==0:
        e.append(x[i])
    else:
        o.append(x[i])
print(sum(e)-sum(o))