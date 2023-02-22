import sys
from collections import deque
input=sys.stdin.readline

n,m,start=map(int,input().split())
#간선그래프
graph=[]
#방문표시
visited_bfs=[False]*(n+1)
visited_dfs=[False]*(n+1)

for i in range(m):
  [a,b]=list(map(int,input().split()))
  graph.append([a,b])
  graph.append([b,a])

#print(graph)
#단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
graph.sort()
#print(graph)
#print(visited)


def bfs(start):
  #들어온거 방문처리
  visited_bfs[start]=True
  answer=[]
  answer.append(start)
  d=deque()
  d.append(start)
  
  while d:
    num=d.popleft()
    for [x,y] in graph:
      if (x==num and not visited_bfs[y]):
        d.append(y)
        answer.append(y)
        visited_bfs[y]=True
      if (y==num and not visited_bfs[x]):
        d.append(x)
        answer.append(x)
        visited_bfs[x]=True
  
  return answer
answer_dfs=[]

def dfs(start):
  #들어온거 방문처리
  visited_dfs[start]=True
  
  answer_dfs.append(start)
  for [x,y] in graph:
    if (x==start and not visited_dfs[y]):
      #answer_dfs.append(y)
      dfs(y)
    elif (y==start and not visited_dfs[x]):
      #answer_dfs.append(x)
      dfs(x)
  
  return answer_dfs



print(*dfs(start))
print(*bfs(start))


  
