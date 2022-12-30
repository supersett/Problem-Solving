import sys

#2차원 정렬을 사용해야할것 같다.

n=int(sys.stdin.readline())
target=[]

for _ in range(n):
  x,y=map(int,sys.stdin.readline().split())
  target.append([x,y])

target.sort(key=lambda x:(x[1],x[0]))

#print(target)

for i in target:
  x,y=i
  x=str(x)
  y=str(y)
  print(x+' '+y)
  