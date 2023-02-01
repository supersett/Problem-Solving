import sys

input=sys.stdin.readline

max_num=0
now_num=0
for _ in range(10):
  x,y=map(int,input().split())
  now_num-=x
  now_num+=y
  if now_num>=max_num:
    max_num=now_num

print(max_num)