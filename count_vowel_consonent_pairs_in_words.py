def fun(n):
    v='aeiou'
    i=0
    j=len(n)-1
    c=0
    while i<j:
        if ((n[i] in v and n[j] not in v) or (n[j] in v and n[i] not in v)) and n[i]!=' ' and n[j]!=' ':
            c+=1
        i+=1
        j-=1
    return c
n=input()
n=n.lower()
s=n.split()
c=0
for i in s:
    c+=fun(i)
print(c)