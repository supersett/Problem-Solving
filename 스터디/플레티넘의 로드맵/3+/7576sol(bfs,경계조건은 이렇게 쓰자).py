#진짜개짜쯩ㅇ짜아짜ㅏ아아짜
#원표 풀이 : https://www.acmicpc.net/source/47390787
from collections import deque
import sys
#y=i
m,n=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#print(graph)
q=deque([])
res=0

for y in range(n):
    for x in range(m):
        if graph[y][x]==1:
            q.append((x,y))
#print(q)
def bfs():
    while q:
        x,y=q.popleft()
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
        
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                q.append((nx,ny))
                graph[ny][nx]=graph[y][x]+1

bfs()
#print(graph)
# if any(0 in l for l in graph):
#     print(0)

for i in graph:
    for j in i:
        if j ==0:
            print(-1)
            exit(0)
    res=max(res,max(i))
print(res-1)
