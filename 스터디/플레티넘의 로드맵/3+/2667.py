from collections import deque
import sys
sys.setrecursionlimit(10000)

n=int(input())
g=[]
answer=[]
for _ in range(n):
    g.append(list(input()))
#print(g)
#d=[[0 for j in range(n)] for i in range(n)]
#여기다가 이제 체크를 해줄 예정이다.
graph=[[0]*n for i in range(n)]

def dfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if g[y][x]=='1':
        global cnt_단지
        cnt_단지+=1
        g[y][x]='0'
        for i in range(4):
            nx=x+dx[i]    
            ny=y+dy[i]    
            dfs(nx,ny)
    return(cnt_단지)
cnt=0
cnt_단지=0
for x in range(n):
    for y in range(n):
        if g[y][x]=='1':
            answer.append(dfs(x,y))
            cnt_단지=0
            cnt+=1

answer.sort()
print(cnt)
for i in answer:
    print(i)


    
#def bfs()
    



