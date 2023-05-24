def iso(n):
    for i in n:
        if n.count(i)!=1:
            return False
    return True
n=input()
if iso(n):
    print('True')
else:
    print('False')