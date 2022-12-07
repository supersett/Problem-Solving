import sys
from collections import defaultdict
import operator

input=sys.stdin.readline

N,M,B=map(int,(input().rstrip().split()))

#print(B)
d=defaultdict(int)
total_ground=0
target=[]
for _ in range(N):
  list_input=list(map(int,input().rstrip().split()))
  #print(list_input)
  for i in list_input:
    total_ground+=i
    d[i]+=1

#다 돌고나오면 총 땅갯수랑 현재상태가 저장된 딕트를 알수있음
#print(total_ground)
#print(target)
d1=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
d_sorted=dict(d1)
#이거 맞냐 누가봐도 아닌것같은데?
print(d_sorted)

for key,value in d_sorted.items():
  
  
  