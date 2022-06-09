import sys

n=int(sys.stdin.readline())

mycard=list(map(int,sys.stdin.readline().split()))
#print(mycard)

m=int(sys.stdin.readline())
sangcard=list(map(int,sys.stdin.readline().split()))

mycard_set=set(mycard)
result=[]
for x in sangcard:
    if x in mycard_set:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))