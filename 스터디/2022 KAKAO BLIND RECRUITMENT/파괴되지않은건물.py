def solution(board, skill):
    answer = 0
    
    def change(type,r1,c1,r2,c2,degree):
      if type==1:
        degree=degree*(-1)
      for i in range(r1,r2+1):
        for j in range(c1,c2+1):
          board[i][j]+=degree
    
    for A_skill in skill:
      type,r1,c1,r2,c2,degree=A_skill
      change(type,r1,c1,r2,c2,degree)
    
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j]>0:
          answer+=1
    
    return answer
  
#solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])