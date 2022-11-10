import sys
from itertools import combinations, permutations
from collections import defaultdict
nums = [1,2,3,4]
perm = list(combinations(nums, 2))

#2
#3
N=int(sys.stdin.readline())
answerlist=[]

for _ in range(N):
  M=int(sys.stdin.readline())
  dic=defaultdict(list)
  for i in range(M):
    name,where=sys.stdin.readline().rstrip().split()
    if dic[where]:
      dic[where]+=[name]
    else:
      dic[where]=[name]
  #print(dic)
  #{'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']})
  #print(len(dic))
  answer=[]
  for key,value_list in dic.items():
    answer_part=len(value_list)
    #print(answer_part)
    answer.append(answer_part+1)
  #print(answer)
  target=1
  for i in answer:
    target*=i
  answerlist.append(target-1)
  
for i in answerlist:
  print(i)
    