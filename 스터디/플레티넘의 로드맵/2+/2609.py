import sys
import math

n,m=map(int,sys.stdin.readline().split())


#최대공약수
print(math.gcd(n,m))
#최소공배수
print(math.lcm(n,m))