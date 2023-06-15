n=input()
s=''
for i in n:
    if int(i)%2!=0:
        s+=str(int(i)**2)
print(s)