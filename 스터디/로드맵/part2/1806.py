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
  
