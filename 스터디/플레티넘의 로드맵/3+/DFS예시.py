def dfs(graph, n, visited):
      # 현재 노드를 방문처리
  visited[n] = True
  print(n, end='')
  
  # 현재 노드와 인접한 노드를 확인
  for i in graph[n]:
    # 방문하지 않은 노드라면
    if not visited[n]:
      # 재귀호출
      dfs(graph, i, visited)

######## dfs 사용
# 각 노드에 연결된 정보를 2차원 리스트로 표현
graph =[
  [], # 노드번호가 1부터 시작하기 때문에 인덱스 0은 비워둔다
  [2,3,8], # 1번 노드와 인접한 노드 2,3,8
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보
visited = [False]*(8+1) # 전체 노드갯수 8개+인덱스0
# dfs 호출
dfs(graph, 1, visited)