import sys

N,M=map(int,sys.stdin.readline().split())
target=list(map(int,sys.stdin.readline().split()))

test=[]
answer=[]

for i in range(M):
  i,j=map(int,sys.stdin.readline().split())
  
  answer.append(sum(target[i-1:j]))

for i in answer:
  print(i)