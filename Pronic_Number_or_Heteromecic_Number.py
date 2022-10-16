n=int(input())
i=0
for i in range(n):
    if(i*(i+1)==n):
        i=1
        break
if i==1:
    print("YES")
else:
    print("NO")