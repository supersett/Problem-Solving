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

N=int(input())
target=list(map(int,input().split()))
count=0
#print(target)

for i in target:
  if check(i):
    count+=1

print(count)