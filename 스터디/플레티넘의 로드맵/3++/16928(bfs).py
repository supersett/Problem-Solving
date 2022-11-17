import sys
from collections import deque,defaultdict

N,M=map(int,sys.stdin.readline().split())
dic=defaultdict(list)
for i in range(N+M):
  start,end=map(int,sys.stdin.readline().split())
  dic[start]=end

dic = sorted(dic.items(), key=lambda x:-x[1])
dic=dict(dic)
print(dic)
#해당 위치까지 걸린 최소 수를 저장해줄 예정
visited=[0]*110


def bfs(now):
  q=deque()
  q.append(now)
  visited[now]=0
  
  while q:
    check=q.popleft()
    for i in range(1,7):
      new=check+i
      #주사위를 굴려 100에 도달하면 종료
      #아 이동이 아니라 해당위치를 바로 반환을 해줘야 하는구나......
      # 대입이 아니었어
      if visited[new]==0:
        visited[new]=visited[check]+1
      else:
        visited[check]=visited[new]
      
      
      #사다리 있는지 찾기
      if new in dic:
        visited[dic[new]]=visited[new]
        
        
        
    if check>100:
      break
    q.append(check+6)
    

bfs(1)
print(visited[100])
      