from collections import defaultdict
import operator
import copy
def solution(n, student, point):
    answer = 0
    #우열반멤버가 바뀌었는지 체크
    #[학생번호,학생점수]
    #paper=[[i+1,0] for i in range(n)]
    dic={}
    for i in range(1,n+1):
      dic[i]=0
    #print(dic)
    #{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    #
    print(dic)
    high=set()
    test=set()
    list_high=[]
    #우열반 편성
    dic = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
    dic=dict(dic)
    for key,value in dic.items():
      list_high.append([key,value])
    for i in range(3):
      high.add(list_high[i][0])
    list_high.clear()
      
    
    for i,j in zip(student,point):
      dic[i]+=j
      dic = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
      dic=dict(dic)
      for key,value in dic.items():
        list_high.append([key,value])
      #print(list_high)
      for i in range(3):
        test.add(list_high[i][0])
      #print(test)
      list_high.clear()
      if test!=high:
        answer+=1
        high=copy.deepcopy(test)
        test.clear()
      test.clear()
      
    return answer
print(solution(6,[6,1,4,2,5,1,3,3,1,6,5],[3,2,5,3,4,2,4,2,3,2,2]))