import sys
target=[]
answer=0
tmp=0
N,K=map(int,sys.stdin.readline().split())
for _ in range(N):
  target.append(int(sys.stdin.readline().rstrip()))

target.sort(reverse=True)
#print(target)

for i in target:
  if K>=i:
    answer+=K//i
    K=K%i
print(answer)