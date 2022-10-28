from itertools import permutations


def solution(A, B):
    answer = 0
    target=[]
    perm=list(permutations(B,len(B)))
    
    for case in perm:
      answer=0
      for i in range(len(A)):
        if case[i]>A[i]:
          answer+=1
      target.append(answer)
          
    
    return max(target)

#7531
#8521