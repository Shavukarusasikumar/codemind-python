a=list(map(str,input().split()))
b=a[0]
for i in a:
    if len(i)<=len(b):
        b=i
print(len(b))