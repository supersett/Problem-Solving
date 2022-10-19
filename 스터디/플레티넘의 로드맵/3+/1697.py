from collections import deque

n,m=map(int,input().split())


def bfs(n,m):
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x==m:
            print(dist[x])
            break
        for nx in (x-1,x+1,x*2):
            if 0<=nx<=max and not dist[nx]:
                dist[nx]=dist[x]+1
                q.append(nx)

max=10**5
#이동거리를 알기위한 변수
dist=[0]*(max+1)


bfs(n,m)
    

