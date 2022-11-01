n=int(input())
x=map(int,input().split())
e=[]
for i in x:
    if i%2!=0:
        e.append(i)
print(sum(e))