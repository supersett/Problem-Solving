# [아이디어]
# stack을 두개정도 사용할거임.

# target에는 주어진 괄호들이 들어있는상황.

# a에는 target에서 빼온 문자를 순서대로 넣을거고
# b에는 숫자로 변환 된 값들을 넣어줄거고 최종적으로 더해줄거임

# a에 넣을때 1.잘 닫히는지(문제없는 문자열인지) 2.닫혔을때 안에 값 계산

import sys
from collections import deque

target=list(sys.stdin.readline().rstrip())

#print(target)
d=deque(target)
stack_a=deque()
stack_b=deque()
make=True
answer=0

for _ in range(len(target)):
  #괄호열 맨 왼쪽부터 검사
  num=d.popleft()
  
  if num ==']' or num ==')':
    #닫는 괄호가 나왔을때 앞에 아무것도 없다면 잘못된 괄호열
    if not stack_a:
      make=False
      break
    #괄호의 짝이 맞지 않다면 잘못된 괄호열
    if (num==']' and stack_a[-1]=='(') or (num==')' and stack_a[-1]=='[]'):
      make=False
      break
    
    #(()[[]])([])
    #2 4 
    #4
    #[()()]
    #2*(2+3*3)
    #[[][]] 쉽지 않네 ㅅㅂ
    #이제 괄호열을 계산해주어야 한다.
    if num==']':
      stack_a.pop()
      #그냥 덧셈만 하면 됨
      if stack_a:
        stack_b.append(3)
      else:
        if not stack_b:
          answer+=3
        else:
          answer+=(sum(stack_b)*3)
          stack_b.clear()
          
    if num==')':
      stack_a.pop()
      #그냥 덧셈만 하면 됨
      if stack_a:
        stack_b.append(2)
      else:
        if not stack_b:
          answer+=2
        else:
          answer+=(sum(stack_b)*2)
          stack_b.clear()
  else:
    stack_a.append(num)

if make:
  print(answer)
else:
  print(0)

