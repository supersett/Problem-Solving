import math

def solution(n,words):
    answer=[]
    nth_count=0
    s=set()
    
    for i in range(len(words)):
        #중복되면 아웃 중복되지 않으면 집합에 추가
        nth_count+=1
        if words[i] not in s:
            s.add(words[i])
        else:
            man_n=nth_count%n
            if man_n==0:
                man_n=n
            man_count=(nth_count/n)
            
            if man_count==0:
                man_count=1
            answer.append(man_n)
            answer.append(math.ceil(man_count))
            return answer
        
        if i>=1:
            #앞단어와 끝말잇기가 성사가 안되면 아웃
            if words[i-1][-1]!=words[i][0]:
                man_n=nth_count%n
                if man_n==0:
                    man_n=n
                man_count=(nth_count/n)
                if man_count==0:
                    man_count=1
                answer.append(man_n)
                answer.append(math.ceil(man_count))
                return answer
    
    answer=[0,0]
    return answer

#solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
    
    
    