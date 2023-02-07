import sys
input=sys.stdin.readline

def check(n):
  machine=True
  if n==1:
    return False
  
  for i in range(2,int(n**(0.5)+1)):
    if n%i==0:
      machine=False
  
  return machine

M=int(input())
N=int(input())
answer=0
min_num=10001

for i in range(M,N+1):
  if check(i):
    answer+=i
    if i<min_num:
      min_num=i

if answer==0:
  print(-1)
else:
  print(answer)
  print(min_num)