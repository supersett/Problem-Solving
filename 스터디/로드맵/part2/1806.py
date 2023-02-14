import sys
from collections import deque

input=sys.stdin.readline

n,s=map(int,input().split())
target=list(map(int,input().split()))
tmp=0
#앞포인트
point_front=0
#뒤포인트
point_back=0
min_length=sys.maxsize
switch=True

while switch:
  #시작,뒤 까지 다 더해
  
  if tmp>=s:
    min_length=min(min_length,point_back-point_front)
    
    #문제 접근 로직은 맞았는데 경계조건에서 반례 뚜들겨 맞으면서 시간이 오래걸림
    #현재 자신 위치를 먼저 연산을 해야지.
    #더하고나서 연산을 해버리면 point_front 0은 영영 계산을 못해.
    #1.더하고 연산할지
    #2.연산하고 더할지 
    #판단하는 기준은 모든걸 훑을 수 있는지 봐야한다.
    #1번이 안되는 이유는 더하는 순간 0인 지점은 내가 체크를 누락하게됨.
    #앞으로 이런 상황이 생기면 꼭 다 훑기 가능한지 찬찬히 따져보자.
    
    tmp-=target[point_front]
    point_front+=1
  else:
    if point_back==n:
      switch=False
      break
    else:
      tmp+=target[point_back]
      point_back+=1

if min_length==sys.maxsize:
  print(0)
else:
  print(min_length)
  
