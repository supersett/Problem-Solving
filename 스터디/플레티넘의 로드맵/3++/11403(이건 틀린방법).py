import sys
from collections import deque,defaultdict
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline().rstrip())
graph=[(list(map(int,sys.stdin.readline().split()))) for i in range(N)]

print(graph)

dic=defaultdict(set)

def dfs(now):
  global N
  if not dic[now]:
    for i in range(N):
      if graph[now-1][i]==1:
        if (i+1) not in dic[now]:
          dic[now].add(i+1)
          dfs(i+1)
        else:
          break
  else:
    return
for i in range(1,N+1):
  dfs(i)
print(dic)

      
