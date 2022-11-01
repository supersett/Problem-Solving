def solution(board, skill):
    answer = 0
    tmp=[[0]*(len(board[0])+1) for i in range(len(board)+1)]
    
    for type,r1,c1,r2,c2,degree in skill:
      if type==1:
        degree=degree*(-1)
      tmp[r1][c1]-=degree
      tmp[r1][c2+1]+=degree
      tmp[r2+1][c1]+=degree
      tmp[r2+1][c2+1]-=degree
    
    
    
    #행 기준 누적합  
    for i in range(len(tmp)-1):
      for j in range(len(tmp[0])-1):
        tmp[i][j+1]+=tmp[i][j]
    
    #열 기준 누적합
    for j in range(len(tmp[0])-1):
      for i in range(len(tmp)-1):
        tmp[i][j+1]+=tmp[i][j]
    
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            # board에 값이 1이상인 경우 answer++
            if board[i][j] > 0: answer += 1
    
    return answer


#solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])