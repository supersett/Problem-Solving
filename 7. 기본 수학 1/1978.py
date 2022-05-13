import sys
import math
n=int(sys.stdin.readline())
count=0
def primenum(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

k=list(map(int,sys.stdin.readline().split()))

for x in k:
    if primenum(x) is True:
        if x!=1:
            count+=1

print(count)