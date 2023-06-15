x=input()
n=list(x)
k=n[-2]+n[-1]
for _ in range(3):
    n.pop(-1)
c=int(n[0]+n[1])
d=str(c+12)
if c==12 and k=='AM':
    n[0],n[1]='0','0'
    print(''.join(n))
elif c==12 and k=='PM':
#     n[0],n[1]='2','4'
    print(''.join(n))
elif c<12 and k=='AM':
    print(''.join(n))
else:
    n[0],n[1]=d[0],d[1]
    print(''.join(n))
# print(k)