from collections import deque

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    deq_A=deque(A)    
    deq_B=deque(B)
    
    for _ in range(len(deq_A)):
      if deq_A[0]>=deq_B[0]:
        deq_B.popleft()
      else:
        deq_A.popleft()
        deq_B.popleft()
        answer+=1
    return answer