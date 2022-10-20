import sys

n,m=map(int,sys.stdin.readline().split())
graph=[]
for i in range(m):
    k=list(map(int,sys.stdin.readline().split()))
    graph.append(k)

    
if all(0 not in l for l in graph):
    print("0이 없어")
else:
    print("0이 있어")

