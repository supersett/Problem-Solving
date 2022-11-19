import sys
from collections import deque

q=deque()
N=int(sys.stdin.readline().rstrip())
answer=[]

for _ in range(N):
  input=int(sys.stdin.readline().rstrip())
  if input!=0:
    q.append([abs(input),input])

  else:
    if not q:
      answer.append(0)
      continue
    q=list(q)
    q.sort()
    q=deque(q)
    target=q.popleft()
    answer.append(target[1])

for i in answer:
  print(i)

    