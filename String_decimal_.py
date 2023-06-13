def fun(n):
    for i in n:
        if i.isalpha():
            return 'False'
    return 'True'
for _ in range(int(input())):
    n=input()
    print(fun(n))