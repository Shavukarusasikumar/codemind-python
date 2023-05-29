n=input()
a=n.split()
s1,s2=0,0
for x in a:
    i=list(x)
    i.sort()
    s1+=ord(i[0])
    s2+=ord(i[-1])
print(s2-s1)