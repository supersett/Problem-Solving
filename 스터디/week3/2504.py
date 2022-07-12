import sys
t=sys.stdin.readline().rstrip()
stack=[]
answer=0
temp=1

for i in range(len(t)):
    if t[i]=="(":
        temp*=2
        stack.append(t[i])
    elif t[i]=="[":
        temp*=3
        stack.append(t[i])
    elif t[i]==")":
        if not stack:
            answer=0
            break
        if stack[-1]=="[":
            answer=0
            break
        if t[i-1]=="(":
            answer+=temp
        stack.pop()
        temp//=2
    else:
        if not stack:
            answer = 0
            break
        if stack[-1] == '(':
            answer = 0
            break
        if t[i-1] == '[':
            answer += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)