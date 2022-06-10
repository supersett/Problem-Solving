import math
import sys

m=int(sys.stdin.readline())
n=int(sys.stdin.readline())
data=[]
def primenum(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
for i in range(m,n+1):
    if primenum(i) is True:
        if i!=1:
            data.append(i)
if len(data)!=0:
    print(sum(data))
    print(min(data))
else:
    print(-1)