import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
d=list(str(a*b*c))
for x in range(0,10):
    x=str(x)
    print(d.count(x))