def rev(num):
    r=0
    while num:
        d=num%10
        num=num//10
        r=r*10+d
    return r

num=int(input())
a=rev(num)
if(a==num):
    print("True")
else:
    print("False")
