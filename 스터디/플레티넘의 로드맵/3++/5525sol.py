import sys
from collections import deque

N=int(sys.stdin.readline().rstrip())
M=int(sys.stdin.readline().rstrip())
S=list(sys.stdin.readline().rstrip())

# N=1 -> ioi -> len=3
# N=2 -> ioioi -> len=5

count=0
#S=OOIOIOIOIIOII
len_target=(2*N+1)
target='I'
for i in range(N):
  target+='OI'
  
q=deque()
target=deque(S)


while True:
  t=target.popleft()
  if not q:
    if t=='I':
      q.append(t)
  else:
    #같다면 안됨
    if q[-1]==t:
      
