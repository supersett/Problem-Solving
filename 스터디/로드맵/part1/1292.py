import sys
input=sys.stdin.readline

a,b=map(int,input().split())
target=[]
k=0
point=0
answer=0

for i in range(1,b+1):
  k+=i
  if b <=k:
    point=i
    break
  
#print(point)
for i in range(1,point+1):
  target+=[i]*i

#print(target)
for i in range(a-1,b):
  answer+=target[i]

print(answer)