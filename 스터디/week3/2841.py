import sys
#t = 음 갯수, s=프렛의 수
t,s=map(int,sys.stdin.readline().split())

data=[]
#줄이 다른걸 이렇게 처리할 수가 있구나!!! 아예 스택을 2차원배열로하는거야!
stack=[[] for _ in range(t)]
cnt=0
#입력된 값들 [x,y] 형태로 리스트에 집어넣음. 이제 꺼내 쓰면된다.
for i in range(t):
    x,y=map(int,sys.stdin.readline().split())
    data.append([x,y])

#여기서 쓸 원리는 일단 
#1. 아무것도 없으면 카운트+1 , 스택에 쌓기
#2. 다음 들어온 값이 전 값보다 낮으면 지금 들어온 값보다 큰 값들을 스택에서
# 지워준다(cnt+=1) 스택에 추가한다(cnt+=1)
#3. 전 값보다 크면 cnt+=1, 스택에 추가
#아니 줄이 다른건 어떻게 처리하냐 하
for i in range(len(data)):
    #스택이 아예 비었을때(처음 음을 연주 시작할때)
    if not stack:
        cnt+=1
        stack.append(data[i])
    #연주 중간
    else:
        # 리스트에 있는 음이 들어왔을 경우
        if data[i][0] in stack[0]:
             
             #같은 음 기준으로 기존에 있는것보다 큰 프랫이 들어왔을 경우
             if 
             
             

        # 리스트에 없는 음이 들어왔을 경우
        else :
            


