from collections import deque
import sys

#전형적인 bfs 문제인것같다.
#인접한곳을 찾아서 같은 값으로 변경해준다. 0->1로
#-> 함수를 하나 만들어서 변경해줄예정
#근데 이제 하나의 요소가 첨가됨
#rg / b 를 구분하는 함수 하나 -  A
#r / g / b 를 구분하는 함수 하나 -  B
#visited를 두개 만들지 하나를 만들지 (하나를 만든다면 깊은복사를 사용하고
# 두개를 만든다면 깊은복사를 안해도 괜찮을듯)
#함수를 구현한뒤, 모든 그래프를 순환하면서 A,B를 진행한다 -> visited 두개만들자
#그러면서 answer_not_rg / answer_rg 의 값을 하나씩 추가해 나가자
#함수 2개 만들기 -> 그래프 순환하면서 answer에 구역 더해나가기 -> 출력하기 끝!

N=int(sys.stdin.readline())
graph=[list(sys.stdin.readline().rstrip()) for i in range(N)]
#graph 잘 입력 받았음
#print(graph)
visited_rg=[[0 for i in range(N)] for i in range(N)]
visited=[[0 for i in range(N)] for i in range(N)]
answer_rg=0
answer=0
target=[]

#print(visited_rg)
#함수를 두개 만들예정
def bfs_for_rg(x,y):
  q=deque()
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  #현재위치 방문표시
  visited_rg[x][y]=1
  now_color=graph[x][y]
  q.append((x,y))
  while q:
    now_x,now_y=q.popleft()
    for i in range(4):
      nx=now_x+dx[i]
      ny=now_y+dy[i]
      
      if 0<=nx<N and 0<=ny<N:
        if now_color=="B":
          if graph[nx][ny]=="B" and visited_rg[nx][ny]==0:
            visited_rg[nx][ny]=1
            q.append((nx,ny))
        else:
          if (graph[nx][ny]=="R" or graph[nx][ny]=="G") and visited_rg[nx][ny]==0:
            visited_rg[nx][ny]=1
            q.append((nx,ny))

def bfs(x,y):
  q=deque()
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  #현재위치 방문표시
  visited[x][y]=1
  now_color=graph[x][y]
  q.append((x,y))
  while q:
    now_x,now_y=q.popleft()
    for i in range(4):
      nx=now_x+dx[i]
      ny=now_y+dy[i]
      
      if 0<=nx<N and 0<=ny<N:
        if now_color=="B":
          if graph[nx][ny]=="B" and visited[nx][ny]==0:
            visited[nx][ny]=1
            q.append((nx,ny))
        elif now_color=="R":
          if graph[nx][ny]=="R" and visited[nx][ny]==0:
            visited[nx][ny]=1
            q.append((nx,ny))
        else:
          if graph[nx][ny]=="G" and visited[nx][ny]==0:
            visited[nx][ny]=1
            q.append((nx,ny))

for x in range(N):
  for y in range(N):
    if visited[x][y]==0:
      bfs(x,y)
      answer+=1
    if visited_rg[x][y]==0:
      bfs_for_rg(x,y)
      answer_rg+=1

target.append(answer)
target.append(answer_rg)

for i in target:
  print(i,end=' ')          
  

