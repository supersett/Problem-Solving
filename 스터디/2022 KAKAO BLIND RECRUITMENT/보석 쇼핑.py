#set으로 총 종류의 보석갯수 구해놓음
#모든 보석을 사는 가장 짧은 구간
from collections import deque

def solution(gems):
  set_gem=set(gems)
  total_count=len(set_gem)
  print(total_count)
  answer=[]
  d=deque(gems)
  left=0
  right=0
  
  for j in range(len(gems)):
    thing=d.popleft()
    if len(set(d))<total_count:
      d.appendleft(thing)
      left=j+1
      break
  for i in range(len(gems)):
    thing=d.pop()
    if len(set(d))<total_count:
      #print(len(set(d)))
      d.append(thing)
      right=len(gems)-i
      break
  answer.append([left,right])
  
  p=deque(gems)
  for i in range(len(gems)):
    thing=p.pop()
    if len(set(p))<total_count:
      #print(len(set(d)))
      p.append(thing)
      right=len(gems)-i
      break
  for j in range(len(gems)):
    thing=p.popleft()
    if len(set(p))<total_count:
      p.appendleft(thing)
      left=j+1
      break
  answer.append([left,right])
  
  return min(answer)

print(solution(["AA", "AB", "AC", "AA", "AC"]))