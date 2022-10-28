from collections import deque
def solution(n, stations, w):
  cover=2*n+1  
  answer = 0
  graph=[0]*(n+1)
  for i in stations:
    for j in range(i-w,i+w+1):
      if j>n:
        continue
      graph[j]=1
      
  d=deque(graph)
  d.popleft()
  while d:
    if d[0]==0:
      answer+=1
      for _ in range(cover):
        if not d:
          continue
        else:
          d.popleft()
    else:
      d.popleft()

  return answer
3 3 1 7891011 12~16