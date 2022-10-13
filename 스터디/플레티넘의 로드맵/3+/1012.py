import sys
sys.setrecursionlimit(10000)

answer=[]
#재귀함수를 만들어줘야함
def dfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<M) and (0<=ny<N):
            if graph[ny][nx]==1:
                graph[ny][nx]=0
                dfs(nx,ny)

#입력받은값을 세팅해
#test case
t=int(input())

for i in range(t):
    M,N,K = map(int, input().split())
    graph=[[0]*M for i in range(N)]
    cnt=0
    
    #배추위치에 1 표시
    for j in range(K):
        x,y=map(int,input().split())
        graph[y][x]=1
    
    #dfs 활용해서 배추 그룹 수 세기
    for x in range(M):
        for y in range(N):
            if graph[y][x]==1:
                dfs(x,y)
                cnt+=1
    #출력해
    answer.append(cnt)

for z in answer:
     print(z)  
    