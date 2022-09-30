import sys

def solution(s):
    
    cnt=0
    cnt_change=0
    
    while True:
        if s=='1':
            break
        else:
            
            list_s=list(s)
            #0의 갯수를 세
            count_0=list_s.count('0')
            cnt+=count_0
            #0을 빼
            s=s.replace('0','')
            #2진수로 변환한 값을 반환
            n = format(len(s),'b')
            s = str(n)
            cnt_change+=1
        
    answer = [cnt_change,cnt]
    return answer


solution("110010101001")