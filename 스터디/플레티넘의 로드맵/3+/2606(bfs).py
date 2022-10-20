import sys
from collections import deque

n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())
graph=[[0]]
for _ in range(m):
    li=list(map(int,sys.stdin.readline().split()))
    graph.append(li)

visited=[False]*(n+1)

def bfs(start,visited,graph):
    q=deque()
    q.append(start)
    visited[start]=True
    count=0
    
    while q:
        n=q.popleft()
        for j in range(1,m+1):
            if n in graph[j]:
                for k in graph[j]:
                    if not visited[k]:
                        q.append(k)
                        visited[k]=True
                        count+=1
    return count

print(bfs(1,visited,graph))  