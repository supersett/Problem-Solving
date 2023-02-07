import sys
input=sys.stdin.readline
from itertools import permutations
from collections import deque
#만들 수 있는 식의 결과가 최대인 것과 최소인 것

N=int(input())
target=list(map(int,input().split()))
a=list(map(int,input().split()))
#갯수
#a=['+','-','*','//']
b=[]

for i in range(1,5):
  b+=[i]*a[i-1]
#print(b)  
  
perm=list(permutations(b,sum(a)))

#print(perm)
min_num=1000000001
max_num=-1000000001

for a_perm_list in perm:
  count=0
  
  for i in range(len(target)):
    if i==0:
      count+=target[i]
    else:
      if a_perm_list[i-1]==1:
        count+=target[i]
      elif a_perm_list[i-1]==2:
        count-=target[i]
      elif a_perm_list[i-1]==3:
        count*=target[i]
      else:
        if count>=0:
          count//=target[i]
        else:
          count=((-count)//target[i])*(-1)
  
  if count <=min_num:
    min_num=count
  if count>=max_num:
    max_num=count
  count=0

print(max_num)
print(min_num)    
    