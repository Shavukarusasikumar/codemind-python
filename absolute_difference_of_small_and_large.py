n=input()
a=n.split()
for x in a:
    i=list(x)
    i.sort()
    print(abs(ord(i[0])-ord(i[-1])),end=' ')