n=int(input())
x=list(map(str,input().split()))
a=''.join(x)
m=a.split('0')
c=0
for i in m:
    if len(i)>c:
        c=len(i)
print(c)