n=input()
c=0
for i in n:
    if i.isdigit():
        c+=1
if c>0:
    print(f"Contains {c} digit")
else:
    print("Doesn't contain digit")