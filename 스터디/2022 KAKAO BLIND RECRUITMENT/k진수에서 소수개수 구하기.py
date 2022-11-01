import string
from collections import deque

def solution(n, k):
    answer = 0
    def convert_recur(num, base):
      number = string.digits + string.ascii_uppercase
      q, r = divmod(num, base)
      return convert_recur(q, base) + number[r] if q else number[r]
    
    def isprime(n):
      if n <= 1: return False
      i = 2
      while i*i <= n:
          if n%i == 0: return False
          i += 1
      return True
    
    target=convert_recur(n,k)
    str=''
    q=deque(list(target))
    s=set(q)
    if '0' not in s:
      if isprime(int(target)):
          answer+=1
    else:  
      for _ in range(len(q)):
        num=q.popleft()
        if num=='0':
          if str!='' and isprime(int(str)):
            answer+=1
            str=''
          else:
            str=''
        else:
          str+=num
    if str!='' and isprime(int(str)):
      answer+=1
    
    return answer

print(solution(797161,3))

# ##
# 0P0처럼 소수 양쪽에 0이 있는 경우
# P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# P처럼 소수 양쪽에 아무것도 없는 경우
# 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
# 예를 들어, 101은 P가 될 수 없습니다.
# ##