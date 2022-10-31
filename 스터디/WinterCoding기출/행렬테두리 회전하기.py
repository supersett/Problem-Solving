import sys

def solution(rows, columns, queries):
    answer = []
    #graph=[[0 for j in range(columns)] for i in range(rows)]
    #graph=[[i for i in range(1,columns+1)] for j in range(rows)]
    
    graph2=[i for i in range(1,rows*columns+1)]
    graph=[]
    for i in range(rows):
      graph.append(graph2[columns*(i):columns*(i+1)])
    
    #print(graph)
    #2,2,5,4
    def change(a,b,c,d):
      count_y=c-a
      count_x=d-b
      target_min=columns*rows
      #첫값 저장
      target=graph[a][b]
      
      for _ in range(count_y):
        graph[a][b]=graph[a+1][b]
        num=graph[a][b]
        a+=1
        target_min=min(target_min,num)
      for _ in range(count_x):
        graph[a][b]=graph[a][b+1]
        num=graph[a][b]
        b+=1
        target_min=min(target_min,num)
      for _ in range(count_y):
        graph[a][b]=graph[a-1][b]
        num=graph[a][b]
        a-=1
        target_min=min(target_min,num)
      for _ in range(count_x):
        graph[a][b]=graph[a][b-1]
        num=graph[a][b]
        b-=1
        target_min=min(target_min,num)
      graph[a][b+1]=target
      target_min=min(target_min,target)
      
      return target_min
    
    for query in queries:
      a,b,c,d=query
      answer.append(change(a-1,b-1,c-1,d-1))
    
    
    return answer
  
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
