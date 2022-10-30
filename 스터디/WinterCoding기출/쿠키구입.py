from collections import deque
def solution(cookie):
    answer = 0
    q=deque(cookie)
    while len(q)==1:
      length=len(q)
      half=length//2
      sum_left=sum(q[0:half-1])
      sum_right=sum(q[half:])
      if sum_left==sum_right:
        answer=sum_left
      elif sum_left>sum_right:
        q.popleft()
      elif sum_right>sum_left:
        q.pop()
    return answer