def p(num):
    pf=0
    for i in range(1,num):
        if(num%i==0):
            pf+=i
    return pf
a=int(input())
b=int(input())
if(p(a)==b and p(b)==a):
    print('Amicable')
else:
    print("Not Amicable")