n=input()
n=n.lower()
a='aeiou'
for i in n:
    if i in a:
        a=a.replace(i,'')
if len(a)==0:
    print(0)
else:
    for i in a:
        print(i,end=' ')


