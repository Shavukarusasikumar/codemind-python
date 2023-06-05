a0,a1,a2=map(int,input().split())
b0,b1,b2=map(int,input().split())
c1,c2=0,0
if a0>b0:
    c1+=1
elif b0>a0:
    c2+=1
if a1>b1:
    c1+=1
elif b1>a1:
    c2+=1
if a2>b2:
    c1+=1
elif b2>a2:
    c2+=1
print(c1,c2)
