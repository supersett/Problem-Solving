import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

#print(A,B)

#일단 정렬을 먼저 해줄 생각이다. a중 작은 값을 b의 큰값에 곱해줄거임

A=sorted(A)
B.sort(reverse=True)

#print(A,B)
ans=0

for i in range(N):
  ans+=(A[i]*B[i])

print(ans)