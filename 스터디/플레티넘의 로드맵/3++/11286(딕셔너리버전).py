import sys
from collections import defaultdict,deque

d=defaultdict(deque)

N=int(sys.stdin.readline().rstrip())
answer=[]
count_not0=0
count_0=0


for _ in range(N):
  input=int(sys.stdin.readline().rstrip())
  if input!=0:
    count_not0+=1
    if input<0:
      d[abs(input)].appendleft(input)
    else:
      d[abs(input)].append(input)
  else:
    count_0+=1
    if count_0>count_not0:
      answer.append(0)
    else:
      answer.append(d[min(d.keys())].popleft())
      if len(d[min(d.keys())])==0:
        d.pop(min(d.keys()))
#print(d)
#print(min(d[1]))
for i in answer:
  print(i)