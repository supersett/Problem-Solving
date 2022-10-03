

def solution(k, dungeons):
    
    dungeons.sort(key=lambda x:(-x[0],x[1]))
    #print(dungeons)
    
    for i in dungeons:
        
    
    answer = -1
    return answer



solution(80,[[80,20],[50,40],[50,10],[30,10]])

#던전돌고 남은 체력
def cal(k,dun):
    return k-dun[1]