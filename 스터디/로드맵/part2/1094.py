import sys
from collections import deque
input=sys.stdin.readline

x=int(input())



def make_2(N):
  target=deque()
  count=0
  while N>0:
    if(N%2==1):
      count+=1
    target.appendleft(N%2)
    N//=2
  
  return count

print(make_2(x))
