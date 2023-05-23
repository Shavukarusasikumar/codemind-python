r,c=map(int,input().split())
mat=[]
e,o=0,0
for i in range(r):
    a=list(map(int,input().split()))
    mat.append(a)
for i in range(r):
    if i%2==0:
        for j in range(c):
            e+=mat[i][j]
    else:
        for j in range(c):
            o+=mat[i][j]
print(e,o)