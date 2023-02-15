import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
M=int(input())
#좌표 정보 입력
co=[]
#방문여부 체크
visited=[False]*N
global tmp
tmp=0

for i in range(M):
  co.append(list(map(int,input().split())))
i_want=list(map(int,input().split()))

global ans
ans=sys.maxsize
d=deque()

def dfs(start,destination):
  while True:
    global ans
    for i in co:
      if i[0]==start:
        d.append(i[2])
        #도착지에 도착하면 시간 다 더한것중에 최소를 초기화해주고 tmp 0으로 초기화
        if i[1]==destination:
          ans=min(ans,sum(d))
          d.clear()
        else:
          dfs(i[1],destination)
    break
  return ans

print(dfs(i_want[0],i_want[1]))

#내가 원하는건 최소비용이야.
#시작점에서 도착점까지 가는데 
