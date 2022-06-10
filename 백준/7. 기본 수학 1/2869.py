import sys
a,b,c=map(int,sys.stdin.readline().split())
this=0
n=1
while True:
    this+=a
    if this>=c:
       print(n)
       break
    this-=b
    n+=1

