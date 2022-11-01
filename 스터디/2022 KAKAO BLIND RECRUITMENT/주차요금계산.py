from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    a,b,c,d=fees
    dic=defaultdict(list)
    
    def calculate_fee(minute):
      if minute<=a:
        return b
      else:
        return b+math.ceil(((minute-a)/c))*d
      
    
    
    for record in records:
      time,car_num,way=record.split()
      h=int(time[0:2].lstrip())
      m=int(time[3:5])
      time_minute=(60*h)+m
      #print(time_minute)
      dic[car_num].append([[time_minute],[way]])
    
    sorted_dic=sorted(dic.items())
    print(sorted_dic)
    #[('0000', [[[360], ['IN']], [[394], ['OUT']], [[1139], ['IN']]]), ('0148', [[[479], ['IN']], [[1149], ['OUT']]]), ('5961', [[[334], ['IN']], [[479], ['OUT']], [[1379], ['IN']], [[1380], ['OUT']]])]

    for i in range(len(sorted_dic)):
      #0000 부터 돌거임
      car,info=sorted_dic[i]
      if len(info)%2==1:
        info.append([[(60*23)+59],['OUT']])
      #계산해줄거임
      min=0
      fee=0
      for k in range(0,len(info)):
        min+=info[k][0][0]*((-1)**(k+1))
      
      fee=calculate_fee(min)
      answer.append(fee)
    #print(answer)
    #print(calculate_fee(1439))
    return answer
  
#solution([1, 461, 1, 10],["00:00 1234 IN"])
