num=int(input())
a=0
if num>0:
    a=a+((num-1)%9+1)
else:
    a=a
print(a)