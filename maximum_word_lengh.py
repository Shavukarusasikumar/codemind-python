a=list(map(str,input().split()))
b=''
for i in a:
    if len(i)>len(b):
        b=i
print(len(b))