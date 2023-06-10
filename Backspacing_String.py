s=input()
t=input()
l1,l2=[],[]
for i in s:
    if i!='#' and i.isalpha():
        l1.append(i)
    if i=='#':
        l1.pop()
for i in t:
    if i!='#' and i.isalpha():
        l2.append(i)
    else:
        l2.pop()
if l1==l2:
    print('True')
else:
    print('False')
    # print(l1,l2)