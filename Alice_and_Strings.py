def fun1(s1,s2):
    s=list(s1)
    x=0
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            x=1
        if x==0:
            s[i]=chr(ord(s[i])+1)
    return ''.join(s)
    
for _ in range(int(input())):
    s1=input()
    s2=input()
    st=fun1(s1,s2)
    while st[0]<s2[0]:
        st=fun1(st,s2)
    if st==s2:
        print('YES')
    else:
        print('NO')
    
    