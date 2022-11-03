from collections import deque,defaultdict
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
graph=[0]
dic=defaultdict(list)

for i in range(m):
  #graph.append(list(map(int,input().split())))
  a,b=map(int,input().split())
  dic[a].append(b)
  dic[b].append(a)
#print(dic)

#visited_boolean=[False for i in range(m+1)]

#print(graph)
#print(visited)
#{1: [3, 4], 3: [1, 4, 2], 4: [1, 5, 3], 5: [4], 2: [3]}
def bfs(number):
  visited_tool=[0 for i in range(n+1)]
  visited_boolean=[False for i in range(n+1)]
  q=deque([])
  q.append(number)
  #현재노드 방문처리
  visited_boolean[number]=True
  
  while q:
    now=q.popleft()
    for i in dic[now]:
      if not visited_boolean[i]:
        q.append(i)
        visited_tool[i]=visited_tool[now]+1
        visited_boolean[i]=True
  total_num=sum(visited_tool)
  return(total_num)
#print(bfs(3))
answer=0
target=sys.maxsize
for i in range(1,n+1):
  tmp=0
  tmp=bfs(i)
  if tmp < target:
    target=tmp
    answer=i
print(answer)
        