import sys

def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
          
T=int(sys.stdin.readline().rstrip())
answer=[]

for _ in range(T):
  M,N,x,y=map(int,sys.stdin.readline().split())
  num=lcm(M,N)
  range_a=num//M
  range_b=num//N
  isAnswerExsist=False
  for a in range(range_a+1):
    for b in range(range_b+1):
      if (M*a+x)==(N*b+y):
        answer.append(M*a+x)
        isAnswerExsist=True
        break
    if isAnswerExsist:
      break
  if not isAnswerExsist:
    answer.append(-1)

for i in answer:
  print(i)

  