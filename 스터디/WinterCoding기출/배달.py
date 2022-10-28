from collections import defaultdict
s=set()
dic_graph=defaultdict(list)
import sys
sys.setrecursionlimit(10000)
#딕셔너리를 써봐???
from collections import deque

def solution(N, road, K):
    answer = 0
    visited=[0]*(N+1)
    stack=deque([])
    #dic형태로 관계가 정리가 됨.
    for i in road:
      a,b,c=i
      dic_graph[a].append([b,c])
    print(dic_graph)
    #{1: [[2, 1], [4, 2]], 2: [[3, 3]], 5: [[2, 2], [3, 1], [4, 2]]})
    def dfs(n):
      if not dic_graph[n]:
        return
      for b,c in dic_graph[n]:
        #stack.append(b)
        if visited[b]==0:
          visited[b]=visited[n]+c
        elif visited[b]>visited[n]+c:
          visited[b]=visited[n]+c
        dfs(b)
    
    dfs(1)
    #print(visited)
    for i in visited:
      if i<=K:
        answer+=1
    
    return answer-1

