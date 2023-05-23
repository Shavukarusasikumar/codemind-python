r,c=map(int,input().split())
mat=[]
s,s1=0,0
for i in range(r):
    a=list(map(int,input().split()))
    mat.append(a)
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            s+=mat[i][j]
        else:
            s1+=mat[i][j]
print(s,s1)