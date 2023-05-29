n=input()
n=n.lower()
v='aeiou'
i=0
j=len(n)-1
c=0
while i<j:
    if ((n[i] in v and n[j] not in v) or (n[j] in v and n[i] not in v)) and n[i]!=' ' and n[j]!=' ':
        c+=1
    i+=1
    j-=1
print(c)