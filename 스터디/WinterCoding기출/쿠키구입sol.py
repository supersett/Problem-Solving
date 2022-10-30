from collections import deque
def solution(cookie):
    answer = 0
    length=len(cookie)
    
    for i in range(length-1):
      
      left_sum=cookie[i]
      left_cursor=i
      right_sum=cookie[i+1]
      right_cursor=i+1
      
      while True:
        if left_sum==right_sum:
          answer=max(answer,left_sum)
        
        if left_cursor>0 and left_sum<=right_sum :
          left_cursor-=1
          left_sum+=cookie[left_cursor]
        elif right_cursor<length-1 and left_sum>=right_sum :
          right_cursor+=1
          right_sum+=cookie[right_cursor]
        else:
          break
    
    return answer