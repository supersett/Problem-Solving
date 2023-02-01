import sys
input=sys.stdin.readline

T=int(input())
answer=[]
whatiwant=[]
for _ in range(T):
  answer.append(list(map(int,input().split())))

#print(answer)

for i in answer:
  target=sorted(i)
  whatiwant.append(target[-3])

for i in whatiwant:
  print(i)