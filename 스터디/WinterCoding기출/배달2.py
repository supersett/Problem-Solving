from collections import defaultdict
dic_graph=defaultdict(list)
import sys
sys.setrecursionlimit(10000)
from collections import deque

def solution(N, road, K):
  answer = 0
  #answer=set([])
  visited=[sys.maxsize]*(N+1)
  visited[1]=0
  #인접한곳의 연결정보 설정.
  for a_road in road:
    a,b,c=a_road
    dic_graph[a].append([b,c])
    dic_graph[b].append([a,c])
  #{1: [[2, 1], [4, 2]], 2: [[1, 1], [3, 3], [5, 2]], 
  # 3: [[2, 3], [5, 1]], 5: [[2, 2], [3, 1], [4, 2]], 4: [[1, 2], [5, 2]]})
  
  def dfs(n):
    stack=deque([])
    stack.append(n)
    while stack:
      target=stack.pop()
      for b,c in dic_graph[target]:
        if visited[target]+c<=K and visited[target]+c<visited[b]:
          visited[b]=visited[target]+c
          stack.append(b)
  dfs(1)
  print(visited)
  for i in visited:
    if i<=K:
      answer+=1
  return answer

