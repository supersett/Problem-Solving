
graph = [[0 for j in range(11)] for i in range(11)]

count=0

def find(x,y,dir):
  nx=0
  ny=0
  if dir=='U':
    ny=1
  elif dir=='D':
    ny=-1
  elif dir=='R':
    nx=1
  elif dir=='L':
    nx=-1
  dx=x+nx
  dy=y+ny
  
  if dx<0 or dx>11 or dy>11 or dy<0:
    return x,y
  
  if (0<=dx<=11) and (0<=dy<11):
    if graph[dy][dx]==0:
      #이동한거리 전꺼에서 더해줌
      graph[dy][dx]=graph[y][x]+1
    else:
      graph[dy][dx]=graph[y][x]
    
  return dx,dy

def solution(dirs):
    answer = 0
    x,y=5,5
    graph[y][x]=1
    for i in dirs:
      x,y=find(x,y,i)
    
    answer=graph[y][x]
    print(answer-1)
    return answer-1

solution("ULURRDLLU")
