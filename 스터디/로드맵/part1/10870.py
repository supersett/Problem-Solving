import sys
input=sys.stdin.readline

N=int(input())

def cal(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return cal(n-1)+cal(n-2)

print(cal(N))
    
