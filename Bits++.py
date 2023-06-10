s=0
for _ in range(int(input())):
    x=input()
    a=list(x)
    a.remove('X')
    for i in range(1,len(a),2):
        if a[i]=='+':
            s+=1
        else:
            s-=1
print(s)