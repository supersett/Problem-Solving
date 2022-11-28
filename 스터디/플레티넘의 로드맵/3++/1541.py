import sys
from collections import deque
input=sys.stdin.readline().rstrip

logic=input()
d=deque(list(logic))
print(d)
#로직1 - 가 들어오면 (괄호를 넣어준다
#로직2 - 가 또 들어오면 전에 ) 닫는다 or 끝날때까지 -가 안들어오면 맨 뒤에
#)를 추가한다
# eval() 함수는 근데 안쓰는게 맞지 않을까? 
# eval을 안쓰고 구현하는방법을 다시 생각해보자.

#일단 그러면 eval 버전을 한번 구현빠르게?
target=[]
tmp=1
start=0

for i in d:
    
  if i =='-':
    if tmp>0:
      target.append(i)
      target.append('(')
      tmp*=-1
    else:
      target.append(')')
      target.append(i)
      target.append('(')
      tmp*=-1
  else:
    target.append(i)

if tmp<0:
  target.append(')')
  
want_str=''.join(target)
print(eval(want_str))