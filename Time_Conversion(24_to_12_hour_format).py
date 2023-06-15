x=input()
n=list(x)
c=int(n[0]+n[1])
if c==0:
    n[0]='1'
    n[1]='2'
    print(''.join(n) + ' AM')
elif c==12:
    print(''.join(n) + ' PM')
elif c<12:
    print(''.join(n)+' AM')
else:
    k=str(abs(12-c))
    if len(k)==1:
        n[0]='0'
        n[1]=k[0]
    else:
        n[0],n[1]=k[0],k[1]
    print(''.join(n)+' PM')
# print(c)
