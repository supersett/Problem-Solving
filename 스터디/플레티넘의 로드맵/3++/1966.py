import sys
from collections import defaultdict,deque

# 들어오는 중요도를 키로, 갯수를 값으로 설정을 해주면서 현재의 값을 확인하면서 출력을해야할지, 맨뒤로 보낼지를 알아야 할듯 하다.
# 일단 deque와, defaultdict(int)가 필요해 보임
# deque가 빌때까지 현재칸(맨앞)을 조회하면서 우선순위가 제일 높은지를 판별하는 로직을 만들자
# 근데 이제 지정된 문서가 몇번째로 인쇄되는지는 어떻게 알수 있을까
# 출력할때 지정위치를 같이 이동시켜줘보자

input=sys.stdin.readline

total_case=int(input())
real_target=[]


for i in range(total_case):
  N,M=map(int,input().split())
  target=list(map(int,input().split()))
  target_sett=[]
  answer=[]
  
  for k in target:
    target_sett.append([k,0])
  target_sett[M][1]=1
  
  target_sett=deque(target_sett)
  target=deque(target)
  count=0
  d=defaultdict(int)
  
  for j in target:
    d[j]+=1
  
  #defaultdict(<class 'int'>, {1: 5, 9: 1})
  #print(d)
  while target_sett:
    num=target_sett.popleft()
    #print(num)
    if max(d.keys())!=num[0]:
      target_sett.append(num)
    else:
      answer.append(num)
      d[num[0]]-=1
      if d[num[0]]==0:
        d.pop(num[0])
  #print(answer)
  
  for x in range(len(answer)):
    if answer[x][1]==1:
      real_target.append(x+1)
      continue

for _ in real_target:
  print(_)
