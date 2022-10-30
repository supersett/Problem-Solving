from collections import defaultdict
s=set()
dic_graph=defaultdict(list)
import sys
sys.setrecursionlimit(10000)
#딕셔너리를 써봐???
from collections import deque

def solution(N, road, K):
    answer = 0
    target=[]
    visited=[0]*(N+1)
    stack=deque([])
    #dic형태로 관계가 정리가 됨.
    for i in road:
      a,b,c=i
      dic_graph[a].append([b,c])
      dic_graph[b].append([a,c])
    print(dic_graph)
    #{1: [[2, 1], [4, 2]], 2: [[3, 3]], 5: [[2, 2], [3, 1], [4, 2]]})
    def dfs(n):
      if visited[n]>K:
        return
      if not dic_graph[n]:
        return
      for b,c in dic_graph[n]:
        #stack.append(b)
        if visited[b]==0:
          visited[b]=visited[n]+c
          if visited[b]<=K:
            target.append(b)
        elif visited[b]>visited[n]+c:
          visited[b]=visited[n]+c
        dfs(b)
    #0 1 4 2 0
    #dfs(1)
    #print(visited)
    for i in visited:
      if i<=K:
        answer+=1
    
    return answer-1

