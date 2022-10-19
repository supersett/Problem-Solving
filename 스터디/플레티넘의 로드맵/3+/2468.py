from collections import deque
import sys
    
#n=int(input().rstrip())
#done=set([])
graph=[]

def bfs(x,y,h):
    q=deque()
    q.append((x,y))
    #count=0
    #sink_table[x][y]= True
    while q:
        x,y=q.popleft()
        #done.add((x,y))
        dx=[0,0,-1,1]    
        dy=[1,-1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=N or ny>=N or nx<0 or ny<0:
                continue
            if not sink_table[nx][ny] and water_board[nx][ny] > h:
                #count+=1
                sink_table[nx][ny] = True
                q.append((nx,ny))



#for _ in range(n):
#    graph.append(list(map(int,input().split())))

#print(graph)
N = int(sys.stdin.readline().rstrip())
water_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#입력값에 따른 물 높이 board 생성

#물에 잠김 여부를 확인할 수 있는 Boolean Table 생성.
# sink_table = [[False for i in range(N)] for j in range(N)]


#그래프에 있는 값들을 특정 숫자로 바꿔주는 알고리즘이 필요하겠네

ans = 1
for k in range(max(map(max, water_board))):
    sink_table = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if water_board[i][j] > k and not sink_table[i][j]:
                count += 1
                sink_table[i][j] = True
                bfs(i, j, k)
    ans = max(ans, count)

print(ans)