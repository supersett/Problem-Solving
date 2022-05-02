import sys
n,x=map(int,sys.stdin.readline().split())

data=list(map(int,sys.stdin.readline().split()))

for y in range(n):
    if data[y]<x:
        print(data[y],end=" ")