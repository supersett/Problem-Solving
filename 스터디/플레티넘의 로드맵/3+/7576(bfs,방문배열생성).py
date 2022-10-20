#큰거 왔다
from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
graph=[]
for i in range(m):
    k=list(map(int,sys.stdin.readline().split()))
    graph.append(k)
    
#print(graph)
#visited=[[[False]*n] in range(m)]
visited=[[False]*n for _ in range(m)]
visited_2=[[False]*n for _ in range(m)]
#print(visited)
def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[y][x]=True
    count=0
    
    a,b=q.popleft()
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
            
        if nx>=n or ny>=m or n<0 or m<0:
            continue
        if graph[ny][nx]==0 and not visited[ny][nx]:
            q.append((nx,ny))
            #visited[ny][nx]=True
            graph[ny][nx]=1
            count+=1
    return count

def CheckIfThereIsNo1Nearby0(x,y):
    qu=deque()
    qu.append((x,y))
    visited_2[y][x]=True
    count=0
    
    a,b=qu.popleft()
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
            
        if nx>=n or ny>=m or n<0 or m<0:
            continue
        if graph[ny][nx]==1:
            return "True"
        if graph[ny][nx]==0 and not visited_2[ny][nx]:
            qu.append((nx,ny))
            visited_2[ny][nx]=True
            graph[ny][nx]=1
            count+=1
    return count


#숙성시키는거 생각할게 왤케 많냐

total_day=0
#2차원 배열에서 0이 아예 없나요?


set_u=set([])

for i in range(n):
    for j in range(m):
        if graph[j][i]==0:
            set_u.add(CheckIfThereIsNo1Nearby0(i,j))
            
if all(0 not in l for l in graph):
    print("0이 없어 = 0 출력")
    
elif "1" not in set_u:
    print("-1")
else:
    #2차원 배열에서 0이 하나라도 있나요?
    while any(0 in l for l in graph):
        for i in range(n):
            for j in range(m):
                if graph[j][i]==1 and not visited[j][i]:
                    k=bfs(i,j)
        total_day+=1
    print(total_day)




# 저장될때부터 모든 토마토가 익어있는상태 0이 없는 경우 
# = 0 출력 (브루트포스 사용)

# 토마토가 모두 익지 못하는상황 
# = 1인 지점에서 돌렸는데 count가 0이 반환되는 상황 = -1출력해야함