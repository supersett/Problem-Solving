import sys

#입력된 문자열
t=sys.stdin.readline().rstrip()

#괄호를 만날때마다 스택에 담아둘 예정이다
stack=[]
tmp=1
cnt=0
answer_list=[0]*len(t)
#1+3(1+1+2(1+1(1)))
print(answer_list)
for i in range(len(t)):
    if t[i]!="(" or t[i]!=")":
        answer_list[i]=1
        
    if t[i]=="(":
        answer_list=t[i-1]
        stack.append(t[i])
    elif t[i]==")":
        
        stack.append(t[i])
        
    

