def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def mega(n):
    for i in n:
        i=int(i)
        if not prime(i):
            return False
    return True
n=input()
a=int(n)
if mega(n) and prime(a):
    print('Mega Prime')
else:
    print('Not Mega Prime')