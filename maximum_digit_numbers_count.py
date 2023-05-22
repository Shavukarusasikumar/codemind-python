n=int(input())
x=list(map(str,input().split()))
l=[]
for i in x:
    l.append(len(str(i)))
a=max(l)
for i in x:
    if len(str(i))==a:
        print(i,end=' ')