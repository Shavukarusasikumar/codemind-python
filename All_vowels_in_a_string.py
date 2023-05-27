n=input()
a='AEIOU'
b='aeiou'
for i in n:
    if i in a:
        a=a.replace(i,'')
    elif i in b:
        b=b.replace(i,'')
if len(a)==0 or len(b)==0:
    print('True')
else:
    print('False')