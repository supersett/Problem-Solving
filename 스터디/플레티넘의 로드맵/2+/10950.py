
n=int(input())
answer=[]
for _ in range(n):
  x,y=map(int,input().split())
  answer.append(x+y)

for i in answer:
  print(i)
