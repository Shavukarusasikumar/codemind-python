n=input()
a=list(n)
i=0
j=len(a)-1
k='aeiouAEIOU'
while i<j:
    if a[i] in k and a[j] in k:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-=1
    elif a[i] in k and a[j] not in k:
        j-=1
    elif a[i] not in k and a[j] in k:
        i+=1
    else:
        i+=1
        j-=1
print(''.join(a))