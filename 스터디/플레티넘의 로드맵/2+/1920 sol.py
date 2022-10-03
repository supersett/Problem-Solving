import sys

n=int(sys.stdin.readline().rstrip())

obj=set(map(int,sys.stdin.readline().split()))

#print(obj)

m=int(sys.stdin.readline().rstrip())

tar=list(map(int,sys.stdin.readline().split()))

for i in tar:
    if i in obj:
        print(1)
    else:
        print(0)
    