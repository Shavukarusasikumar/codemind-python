p,r,t=map(int,input().split())
a=p*((1+(r/100))**t)
total="{:.2f}".format(a)
print(total)