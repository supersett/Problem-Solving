import sys
import math

m,n= map(int,sys.stdin.readline().split())

def primenum(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

for y in range(m,n+1):
    if m!=1:
        data=primenum(y)
        if data is True:
            print(y)
