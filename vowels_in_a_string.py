a=input()
b=input()
v='AEIOUaeiou'
if b in a:
    print('True')
    print(a.index(b))
else:
    print('False')