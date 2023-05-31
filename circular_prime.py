def pri(n):
    if n<2:
        return False
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            return False
    return True
n=input()
a=n[::-1]
if pri(int(n)) and pri(int(a)):
    print('circular prime')
elif (not pri(int(n))) and (not pri(int(a))):
    print('not prime')
else:
    print('prime but not a circular prime')