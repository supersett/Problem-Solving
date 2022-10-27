import sys 
from collections import deque,defaultdict
#sys.setrecursionlimit(1000000)

#find_union/ 분리집합
m,n=map(int,sys.stdin.readline().split())

graph=[[]]

graph_dict=defaultdict(list)

visited=[0 for i in range(m+1)]
#{1:[2,5]} , {2:[1]}
#미세먼지여 안녕
#분리집합
for i in range(n):
    fr,to=map(int,sys.stdin.readline().split())
    graph_dict[fr].append(to)
    graph_dict[to].append(fr)
    
#find union - 분리집합
#재귀 -> 함수 호출스택을 계속 쌓는다. 돌아갈 위치도 포인터로 알아둬야함
#main 하나에서 while 하나로 끝내는게 제일 좋음.
#print(graph_dict)
#print(visited)
#구현,dfs,bfs,그리디 집중적으로 공부하는거 추천.
#무기 늘릴 생각
#비트마스킹(비주류)
#문자열 다루는것(구현)
#삼성문제, 코테광탈하면서 풀어봤던 문제들

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