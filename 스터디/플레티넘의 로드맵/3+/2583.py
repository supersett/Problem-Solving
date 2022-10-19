from collections import deque
import sys
#y,x
#5 7
m,n,k=map(int,sys.stdin.readline().split())

graph=[[0]*(n) for i in range(m)]
#print(graph)
#[[0, 2, 4, 4], [1, 1, 2, 5], [4, 0, 6, 2]]
box=[]
for _ in range(k):
    box.append(list(map(int,sys.stdin.readline().split())))

def boxing(li):
    x1=li[0]
    x2=li[2]
    y1=li[1]
    y2=li[3]
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[j][i]=1
for k in box:
    boxing(k)
#print(graph)

def bfs(x,y):
    q=deque()
    q.append((x,y))
    graph[y][x]=1
    count=1
    while q:
        x,y=q.popleft()
        dx=[0,0,-1,1]    
        dy=[-1,1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[ny][nx] == 0:
                count+=1
                graph[ny][nx]=1
                q.append((nx,ny))
    return count

answer=[]

for i in range(n):
    for j in range(m):
        if graph[j][i]==0:
            answer.append(bfs(i,j))
#print(graph)
print(len(answer))
print(*sorted(answer))

