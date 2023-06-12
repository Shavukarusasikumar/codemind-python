for _ in range(int(input())):
    s=int(input())
    n=input()
    n=n.lower()
    n=n.replace(' ','')
    m=0
    for i in n:
        if i.isalpha():
            if n.count(i)==1:
                m=1
                print(i)
                break
    if m==0:
        print(-1)
    # print(n)