import sys
from collections import deque

input=sys.stdin.readline

d=deque()


K=int(input())

for i in range(K):
  num=int(input())
  if num==0:
    d.pop()
  else:
    d.append(num)

if not d:
  print(0)
else:
  print(sum(d))