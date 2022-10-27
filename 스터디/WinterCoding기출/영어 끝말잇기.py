from collections import deque

def solution(n, words):
    answer = []
    q=deque()
    s=set([])
    count=0
    for i in range(len(words)):
        #단어를 하나씩 deque에 담는다(선언하기)        
        q.append(words[i])
        count+=1
        #중복이 된다면 out
        if words[i] not in s:
            s.add(words[i])
        else:
            nth=count%n
            if nth==0:
                nth=n
            nman=count//3
            answer.append(nth)
            answer.append(nman)
            return answer
        #앞에와 끝말잇기가 성사하지 않는다면
        if i>=1:
            if words[i-1][:-1]!=words[i][0]:
                nth=count%n
                if nth==0:
                    nth=n
                nman=count//3
                answer.append(nth)
                answer.append(nman)
                return answer
    answer.append(0)
    answer.append(0)
        
    return answer