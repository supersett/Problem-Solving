#bfs로 풀어라
import sys
from collections import deque
input=sys.stdin.readline
INF=int(1e9)

n=int(input())
m=int(input())

# 주어지는 그래프 정보 담는 N+1개 길이의 리스트
graph=[[] for _ in range(n+1)]
#그래프 정보 초기화
for i in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

#방문처리 기록용
visited=[False]*(n+1)
#거리 테이블 용
distance=[INF]*(n+1)
#어디에서 어디로 갈지
i_want=list(map(int,input().split()))

#방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
def get_smallest_node():
  min_value=INF
  index=0
  for i in range(1,n+1):
    if not visited[i] and distance[i]<min_value:
      min_value=distance[i]
      index=i
  return index

#다익스트라 알고리즘
def dijkstra(start):
  #시작노드 : 시작노드 거리계산 및 방문처리
  distance[start]=0
  visited[start]=True

  #시작노드의 인접한 노드들에 대해 최단거리 계산
  for i in graph[start]:
    distance[i[0]]=i[1]
  
  #시작노드 제외한 n-1개의 다른 노드들 처리
  for _ in range(n-1):
    now=get_smallest_node() #방문 x 하면서 시작노드와 최단거리인 노드 반환
    visited[now]=True # 해당노드 방문처리
    #해당노드의 인접한 노드들 간의 거리 계산
    for next in graph[now]:
      cost=distance[now]+next[1] #시작 ->now 거리 + now-> 인접노드 거리
      if cost<distance[next[0]]:
        distance[next[0]]=cost

dijkstra(i_want[0])
#print(distance)
print(distance[i_want[1]])
  





#여러개의 노드가 존재할때, 특정한 노드에서 출발해서 다른 노드로 가는 최단의 경로를 구할때 사용한다
#음의 간선이 존재하지 않는 양수일 때 정상적으로 동작한다.

#매번 가장 거리가 짧은 노드를 선택해서 임의의 횟수의 과정을 계속적으로 반복한다.

#단계


#최단거리를 기록할 테이블
