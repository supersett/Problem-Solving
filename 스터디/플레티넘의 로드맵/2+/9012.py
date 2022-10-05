import sys
from collections import deque

n=int(sys.stdin.readline().rstrip())

target=[]

for x in range(n):
    target.append(sys.stdin.readline().rstrip())
#print(target)
a=deque([])
b=0
answer=[]
for i in target:
    key=list(i)
    if key[0]==")":
        answer.append("NO")
        continue
    else:
        for j in key:
            if j=="(":
                a.append("(")
            else:
                if len(a)==0:
                    answer.append("NO")
                    b+=1
                    break
                a.pop()
        #print(a)
        if b==0 and len(a)==0:
            answer.append("YES")
        elif b==0 and len(a)!=0:
            answer.append("NO")
        a=deque([])
        b=0
        
for k in answer:
    print(k)
