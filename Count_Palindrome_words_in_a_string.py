a=list(map(str,input().split()))
c=0

for i in a:
    i=i.lower()
    if i==i[::-1]:
        c+=1
print(c)
    