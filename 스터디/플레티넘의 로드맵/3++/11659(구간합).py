import sys

N,M=map(int,sys.stdin.readline().split())
target=list(map(int,sys.stdin.readline().split()))
sum=[0]
tmp=0
for i in target:
  tmp+=i
  sum.append(tmp)
#print(sum)

test=[]
answer=[]

for i in range(M):
  i,j=map(int,sys.stdin.readline().split())
  
  answer.append((sum[j]-sum[i-1]))

for i in answer:
  print(i)


