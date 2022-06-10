import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
sum3=0
for eachSum in combinations(data,3):
    target=sum(eachSum)
    if sum3<target<=m:
        sum3=target
print(sum3)
