s=input()
x=[i for i in range(len(s)+1)]
ans=[]
for i in s:
    if i=='I':
        ans.append(x.pop(0))
    else:
        ans.append(x.pop(-1))
ans.append(x[0])
print(*ans)