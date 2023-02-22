import sys,math
from collections import defaultdict
input=sys.stdin.readline

count=0
count_6or9=0
num=input().rstrip()
d=defaultdict(int)

for i in range(0,10):
  d[i]=0

#print(d)

for i in num:
  d[int(i)]+=1

max_cnt=max(d[0],d[1],d[2],d[3],d[4],d[5],d[7],d[8],(d[6]+d[9]+1)//2)
print(max_cnt)
