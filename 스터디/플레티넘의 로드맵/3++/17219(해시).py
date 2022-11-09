import sys
from collections import defaultdict

N,M=map(int,sys.stdin.readline().split())
dic=defaultdict(list)

for i in range(N):
  site,password=sys.stdin.readline().split()
  dic[site]=password

#print(dic)
answer=[]
for i in range(M):
  answer.append(dic[sys.stdin.readline().rstrip()])

for i in answer:
  print(i)
