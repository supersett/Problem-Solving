import sys
a,b,c=map(int,sys.stdin.readline().split())

i=1
while a+b*i > c*i:
    i+=1
    if i>210000000:
        i=-1
        break
if i==-1:
    print(i)
else:
    print(i+1)

