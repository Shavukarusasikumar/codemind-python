n=int(input())
x=[str(i) for i in range(1,n+1)]
i=n
for _ in range(n):
    s=x[:i]
    print(''.join(s))
    i-=1
