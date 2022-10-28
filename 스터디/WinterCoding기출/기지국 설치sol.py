import math
def solution(n, stations, w):
  cover=2*w+1  
  answer = 0
  now=1
  
  for station in stations:
    length=station-w-now
    if length>0:
      answer+=math.ceil(length/cover)
    now=station+w+1
  
  if n>=now:
    answer+=math.ceil((n-now+1)/cover)
  return answer

