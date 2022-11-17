import sys

N=int(sys.stdin.readline().rstrip())

graph=[]
check_graph=[[False] * N for i in range(N)]
for _ in range(N):
  #M=sys.stdin.readline()
  M=list(map(int,sys.stdin.readline().split()))
  graph.append(M)
#print(graph)
#print(check_graph)
#세팅 완료
#[[0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 1, -1, 0, 1, -1], [0, -1, 1, 0, 1, -1, 0, 1, -1], [0, 1, -1, 1, 0, -1, 0, 1, -1]]


#1. 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
#2. 1이 아닌 경우에는 종이를 같은크기의 종이 9개로 자르고 다시 1 확인

#한줄이 3개면 끝난거임
#결국엔 전부 한번은 돌아야함.
count_1=0
count_ma1=0
count_0=0
# 분할정복으로 풀 수 있습니다.
# 조건이 만족하지 않는경우, 9개로 쪼개서 다시 푸는방식
# 9개로 쪼개는것은 재귀함수를 호출하여 풀고, 전달인자로 그 9개 종이 가장왼쪽위 좌표를 넣는다
# 조건이만족하는경우 해당 색상의 값을 +1 해준다.

def dfs(x,y,n):
  global count_0,count_ma1,count_1
  num_check=graph[x][y]
  
  for i in range(x,x+n):
    for j in range(y,y+n):
      if graph[i][j]!=num_check:
        for k in range(3):
          for l in range(3):
            dfs(x+k*n//3,y+l*n//3,n//3)
        return
  
  if num_check==-1:
    count_ma1+=1
  elif num_check==1:
    count_1+=1
  else:
    count_0+=1

dfs(0,0,N)
print(count_ma1)
print(count_0)
print(count_1)
