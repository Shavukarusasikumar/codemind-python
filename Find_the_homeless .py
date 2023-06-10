n=int(input())
l1,l2=[],[]
for _ in range(n):
    a=int(input())
    l1.append(a)
for _ in range(n):
    a=int(input())
    l2.append(a)
i=0
c=[]
while True:
    if len(l1)==0:
        break
    if l1[0]<=l2[i]:
        l1.pop(0)
        l2.pop(i)
        i=-1
    if len(l1)==0:
        break
    i+=1
    if abs(i)==len(l2):
        c.append(l1[0])
        l1.pop(0)
        i=-1
print(len(c))