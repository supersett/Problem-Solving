from collections import deque
import sys

#두 개의 큐를 나타내는 정수 배열 queue1, queue2가 매개변수로 주어집니다. 
#queue1 = [3, 2, 7, 2]
#queue2 = [4, 6, 5, 1]

#queue = deque([4, 5, 6])

def solution(queue1, queue2):
    que1=deque(queue1)
    que2=deque(queue2)
    sum1=sum(que1)
    sum2=sum(que2)
    
    for i in range(len(queue1)*3):
        if sum1==sum2:
            return i
        if sum1 > sum2:
            n=que1.popleft()
            que2.append(n)
            sum1 -= n
            sum2 += n
        else:
            n=que2.popleft()
            que1.append(n)
            sum2 -= n
            sum1 += n
    return -1
#느낀점
