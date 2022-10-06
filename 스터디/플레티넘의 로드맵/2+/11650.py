import sys

n=int(sys.stdin.readline().rstrip())

target=[]

for _ in range(n):
    n,m=map(int,sys.stdin.readline().split())
    target.append([n,m])

target.sort(key=lambda x:(x[0],x[1]))

for i in target:
    print(str(i[0])+" "+str(i[1]))