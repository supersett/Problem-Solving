import sys
a,b,c=map(int,sys.stdin.readline().split())

x=((c-a)//(a-b))+1
if (c-a)%(a-b)>0:
    x+=1
print(x)