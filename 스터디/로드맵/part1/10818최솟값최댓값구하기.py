import sys

input=sys.stdin.readline

minnum=1111111
maxnum=-1111111

N=int(input())
target=list(map(int,input().split()))

#print(target)

for N in target:
  if N >maxnum:
    maxnum=N
  if N <minnum:
    minnum=N

print(str(minnum)+' '+str(maxnum))