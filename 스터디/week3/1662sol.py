import sys

s=sys.stdin.readline().rstrip()
stack=[]
length=0
temp=""
for c in s:
    if c.isdigit():
        length+=1
        temp=c
    elif c=="(":
        stack.append((temp,length-1))
        length=0
    else:
        multi,preL=stack.pop()
        length=(int(multi)*length)+preL
print(length)