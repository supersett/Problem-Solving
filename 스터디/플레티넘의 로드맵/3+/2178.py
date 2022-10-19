from collections import deque

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input()))
#print(graph)

dx=[0,0,1,-1]
dy=[1,-1,0,0]
done=set([])

def bfs(x,y):
    q=deque()
    q.append((x,y))
    count=0
    print("왜안돼")
    while q:
        now=q.popleft()
        done.add(now)
        count+=1
        if now==(n-1,m-1):
            return count
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if (0<=nx<n-1) and (0<=ny<m-1):
                if graph[nx][ny]=='1' and ((nx,ny) not in done):
                    graph[nx][ny]='0'
                    q.append((nx,ny))
                    done.add((nx,ny))


print(bfs(0,0))
                    
                
        
        


