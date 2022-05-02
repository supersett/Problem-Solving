a,b=map(int,input().split())
c=60*a+b
c=c-45
if (c<0):
    c=c+1440
d=c//60
e=c%60
print(str(d),str(e))