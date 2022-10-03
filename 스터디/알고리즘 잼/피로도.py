

def solution(k, dungeons):
    cnt_list=[]
    
    for i in range(0,len(dungeons)):
        cnt=0    
        if k>= dungeons[0]:
            cal(k,dungeons[i])
            cnt+=1
        
    answer = -1
    return answer



solution(80,[[80,20],[50,40],[50,10],[30,10]])

#던전돌고 남은 체력
def cal(k,dun):
    return k-dun[1]