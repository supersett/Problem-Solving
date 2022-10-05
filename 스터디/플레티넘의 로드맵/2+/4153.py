import sys
from collections import deque

#a,b,c=map(int,sys.stdin.readline().split())

answer=[]

while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==0:
        break
    list_target=[]
    list_target.append(a)
    list_target.append(b)
    list_target.append(c)
    list_target.sort()
    list_target=deque(list_target)
    z=list_target.pop()
    y=list_target.pop()
    x=list_target.pop()
    if (x*x)+(y*y)==(z*z):
        answer.append("right")
    else:
        answer.append("wrong")
for i in answer:
    print(i) 
    
    