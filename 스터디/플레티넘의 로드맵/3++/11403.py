import sys
from collections import deque,defaultdict
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline().rstrip())
graph=[(list(map(int,sys.stdin.readline().split()))) for i in range(N)]
target=defaultdict(list)
#print(graph)

# for i in range(N):
#   for j in range(N):
#     if graph[i][j]==1:
#       target[i+1].append(j+1)

# #print(target)
visited=[[0]*N for i in range(N)]

def bfs(now):
  global N
  d=deque()
  d.append(now)
  check=[0 for _ in range(N)]
  while d:
    q=d.popleft()
    
    for i in range(N):
      if check[i]==0 and graph[q][i]==1:
        d.append(i)
        check[i]=1
        visited[now][i]=1

    
for i in range(0,N):
  bfs(i)

for i in visited:
  print(*i)  

