import sys
N,M=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for i in range(N)]

#print(graph)
#[[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 2, 1, 2, 1]]

def check(x,y):
  answer=0
  #case :0 / 오른쪽으로 3번
  x1,y1=x+1,y
  x2,y2=x+2,y
  x3,y3=x+3,y
  #case0=[[1,0],[2,0],[3,0]]
  if 0<=x<N and 0<=x1<N and 0<=x2<N and 0<=x3<N and 0<=y<M and 0<=y1<M and 0<=y2<M and 0<=y3<M:
    answer=max(answer,graph[x][y]+graph[x1][y1]+graph[x2][y2]+graph[x3][y3])
  case1=[]
  case2=[]
  case3=[]
  
  #case2 : 오른쪽으로 2번(3개 고정)
  x1,y1=x+1,y
  x2,y2=x+2,y
  #x3,y3
  case1.append([2,1])
  case1.append([2,-1])
  case1.append([1,1])
  case1.append([1,-1])
  case1.append([0,1])
  case1.append([0,-1])
  for i in case1:
    x3=x+i[0]
    y3=y+i[1]
    if 0<=x<N and 0<=x1<N and 0<=x2<N and 0<=x3<N and 0<=y<M and 0<=y1<M and 0<=y2<M and 0<=y3<M:
      answer=max(answer,graph[x][y]+graph[x1][y1]+graph[x2][y2]+graph[x3][y3])
  
  #오른쪽으로 1번(2개 고정)
  x1,y1=x+1,y
  #x2,y2
  #x3,y3
  case2.append([[1,2],[1,1]])
  case2.append([[1,1],[1,-1]])
  case2.append([[1,-1],[1,-2]])
  case2.append([[0,2],[0,1]])
  case2.append([[0,1],[0,-1]])
  case2.append([[0,-1],[0,-2]])
  
  case2.append([[0,1],[1,-1]])
  case2.append([[1,1],[0,-1]])
  case2.append([[1,1],[2,1]])
  case2.append([[1,-1],[2,-1]])
  
  case2.append([[1,1],[0,1]])
  case2.append([[1,-1],[0,-1]])
  for i in case2:
    x2=x+i[0][0]
    y2=y+i[0][1]
    x3=x+i[1][0]
    y3=y+i[1][1]
    if 0<=x<N and 0<=x1<N and 0<=x2<N and 0<=x3<N and 0<=y<M and 0<=y1<M and 0<=y2<M and 0<=y3<M:
      answer=max(answer,(graph[x][y]+graph[x1][y1]+graph[x2][y2]+graph[x3][y3]))
  
  #제자리(1개 고정)
  #x1,y1
  #x2,y2
  #x3,y3
  case3.append([[0,1],[0,2],[0,3]])
  case3.append([[0,-1],[0,-2],[0,-3]])
  for i in case3:
    x1=x+i[0][0]
    x2=x+i[1][0]
    x3=x+i[2][0]
    y1=y+i[0][1]
    y2=y+i[1][1]
    y3=y+i[2][1]
    if 0<=x<N and 0<=x1<N and 0<=x2<N and 0<=x3<N and 0<=y<M and 0<=y1<M and 0<=y2<M and 0<=y3<M:
      answer=max(answer,graph[x][y]+graph[x1][y1]+graph[x2][y2]+graph[x3][y3])
  
  #자기자리
  return answer

target=0

for i in range(N):
  for j in range(M):
    target=max(target,check(i,j))
print(target)


