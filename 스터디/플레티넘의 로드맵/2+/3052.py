import sys

input=sys.stdin.readline
s=set()

for i in range(10):
  num=int(input())
  s.add((num%42))
  
print(len(s))
