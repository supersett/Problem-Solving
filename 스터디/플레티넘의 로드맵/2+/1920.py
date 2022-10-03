import sys

n=int(sys.stdin.readline().rstrip())

obj=list(input().split(" "))

#print(obj)

m=int(sys.stdin.readline().rstrip())

tar=list(input().split(" "))

for i in tar:
    if i in obj:
        print(1)
    else:
        print(0)
    