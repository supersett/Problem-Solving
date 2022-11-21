import sys
from collections import deque,defaultdict
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline().rstrip())
graph=[(list(map(int,sys.stdin.readline().split()))) for i in range(N)]
target=defaultdict(list)
print(graph)

for i in range(N):
  for j in range(N):
    if graph[i][j]==1:
      target[i+1].append(j+1)

print(target)
visited=[[0]*N for i in range(N)]

def bfs(now):
  d=deque()
  d.append(now)

  while d:
    check=d.popleft()
    #다음으로 넘어갈 선이 존재한다면
    if check in target.keys():
      for i in range(len(target[check])):
        if visited[check-1][target[check][i]-1]==0:
          visited[check-1][target[check][i]-1]=1
          d.append(target[check][i])
        else:
          break
      #이미 체크를 한 상태    
    
for i in range(1,N+1):
  bfs(i)
print(visited)
        
  

