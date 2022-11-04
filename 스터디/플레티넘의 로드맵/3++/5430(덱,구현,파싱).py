import sys
from collections import deque

input=sys.stdin.readline

T=int(input())

answer=[]

for i in range(T):
  AC=input().rstrip()
  AC_list=deque(list(AC))
  #print(AC_list)
  len_bucket=int(input())
  #bucket=input().rstrip().replace('[','').replace(']','')
  #print(bucket)
  #bucket_list=list(bucket.replace(',',''))
  #print(bucket_list)
  #print(bucket_list)
  #bucket_list=list(map(int,bucket_list))
  #bucket_list=[int(i) for i in bucket_list ]
  #print(bucket_list)
  #d=[1,2,3,4]
  
  d = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
  if len_bucket==0:
    d=deque([])
  d=deque(map(int,d))
  print(d)
  
  
  while len(AC_list)!=0:
    command=AC_list.popleft()

    if command=='R':
      d.reverse()
    elif command=='D':
      if len(d)==0:
        answer.append('error')
        break
      else:
        d.popleft()
    if not AC_list:
      answer.append(list(d))
      break
  
print(answer)
