n=int(input())
x=list(map(int,input().split()))
s=[]
c=0
for i in x:
    if x.count(i)==i:
        s.append(i)
        c+=1
s=set(s)
if sum(s)==0:
    avg=0
else:
    avg=sum(s)/len(s)
if c==0:
    print("-1")
else:
    print("%.2f"%avg)