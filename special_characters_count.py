n=input()
c=0
for i in n:
    if i==' ' or i.isalpha() or i.isdigit():
        continue
    c+=1
print(c)