from collections import deque


def solution(d, budget):
    d.sort()
    q=deque(d)
    answer=0
    while q:
        n=q.popleft()
        if budget-n>=0:
            answer+=1
            budget=budget-n
        else:
            break
    return answer
