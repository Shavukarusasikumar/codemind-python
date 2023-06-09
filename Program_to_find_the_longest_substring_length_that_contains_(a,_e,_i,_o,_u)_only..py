s1=input()
a=list(s1)
s=[]
c=[]
for i in range(len(a)):
    for j in range(i,len(a)):
        p=a[i:j+1]
        s.append(p)
for i in s:
    c1=0
    for j in i:
        if j in 'aeiou':
            c1+=1
        else:
            break
    c.append(c1)
print(max(c))
    
        