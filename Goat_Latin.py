n=input()
a1=n.split()
a=[list(i) for i in a1]
c='maa'
for i in a:
    if i[0] in 'aeiouAEIOU':
        i.append(c)
        c+='a'
    else:
        z=i.pop(0)
        i.append(z)
        i.append(c)
        c+='a'
for i in a:
    print(''.join(i),end=' ')
        
