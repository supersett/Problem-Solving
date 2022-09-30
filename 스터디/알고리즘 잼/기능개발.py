import math

def solution(progresses, speeds):
    
    n=len(progresses)
    list_set=[]
    target=[1]
    for i in range(n):
        day=math.ceil((100-progresses[i])/speeds[i])
        list_set.append(day)
    #list_set=[5 10 1 1 20 1]
    #list_target=[1 1 0 0 1 0]
    #target=[]
    t=list_set[0]
    #target.append(1)
    for j in range(1,len(list_set)):
        if list_set[j] > t:
            target.append(1)
            t=list_set[j]
        else:
            target.append(0)
    #target=[1 1 0 0 1 0]
    answer=[]
    for k in target:
        if k==1:
           answer.append(1)
        elif k==0:
            answer[-1]+=1    
    return answer


#print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]	))

