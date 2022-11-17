#i로시작해
import sys
from collections import deque

N=int(sys.stdin.readline().rstrip())
M=int(sys.stdin.readline().rstrip())
S=sys.stdin.readline().rstrip()

# N=1 -> ioi -> len=3
# N=2 -> ioioi -> len=5

count=0
#S=OOIOIOIOIIOII
len_target=(2*N+1)
target='I'
for i in range(N):
  target+='OI'
#target="IOI"
#print(target)
#print(S[2:5])
i=0
while True:
  if i>=len(S):
    break
  
  if S[i]=='I':
    if (i+(2*N+1))<len(S) and S[i:i+(2*N+1)]==target:
      count+=1
      i+=2
    else:
      i+=1
    
  else:
    i+=1

print(count)
          
    