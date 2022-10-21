import sys 
from collections import deque,defaultdict
#sys.setrecursionlimit(1000000)

#find_union/ 분리집합
m,n=map(int,sys.stdin.readline().split())

graph=[[]]

graph_dict=defaultdict(list)

visited=[0 for i in range(m+1)]
#{1:[2,5]} , {2:[1]}

for i in range(n):
    fr,to=map(int,sys.stdin.readline().split())
    graph_dict[fr].append(to)
    graph_dict[to].append(fr)
#재귀 -> 함수 호출스택을 계속 쌓는다. 돌아갈 위치도 포인터로 알아둬야함
#main 하나에서 while 하나로 끝내는게 제일 좋음.
#print(graph_dict)
#print(visited)

def bfs(x):
    q=deque()
    q.append(x)
    #visited[x]=1
    while q:
        target=q.popleft()
        for i in graph_dict[target]:
            if not visited[i]:
                visited[i]=1
                q.append(i)
count=0
for i in range(1,m+1):
    if not visited[i]:
        bfs(i)
        visited[i]=1
        count+=1
print(count)