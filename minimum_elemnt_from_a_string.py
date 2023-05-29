n=input()
b=n.split()
c=b[-1]
a=list(c)
a.sort()
if a[0].islower():
    print(a[0])
elif a[0].lower() in a:
    print(a[0].lower())
else:
    print(a[0])