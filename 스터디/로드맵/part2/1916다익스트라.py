import sys
import heapq
INF=sys.maxsize
input=sys.stdin.readline

n=int(input())
m=int(input())
graph={}
for i in range(n+1):
  graph[i]={}

#중복되는 경우 cost를 최솟값으로 초기화 해주는 작업
for _ in range(m):
  start,end,cost=map(int,input().split())
  if end in graph[start].keys():
    if graph[start][end]>cost:
      graph[start][end]=cost
  else:
    graph[start][end]=cost

start,end=map(int,input().split())

d=[INF]*(n+1)

#print(graph)
def dijkstra(graph,start):
  d[start]=0
  q=[]
  heapq.heappush(q,[d[start],start])
  #시작 노드 탐색을 위해 초기화
  while q:
    cur_d,cur_dest=heapq.heappop(q)
    
    if d[cur_dest]<cur_d:
      continue
    
    for new_dest,new_d in graph[cur_dest].items():
      tmp_d=cur_d+new_d # 거쳐가는 거리
      if tmp_d<d[new_dest]:
        #현재 최단거리보다 거쳐가는게 더 가까움
        d[new_dest]=tmp_d # 최단거리 갱신
        heapq.heappush(q,[tmp_d,new_dest])
  return d

dijkstra(graph,start)
print(d[end])