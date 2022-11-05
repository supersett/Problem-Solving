from collections import deque
#마지막꺼를 체크
#이 알고리즘을 쓰면 끝까지 풀릴것같은데?
#무슨상황에서 무슨 해결방법을
#문제마다 분기점이생기는데 뚜렷하게 뭘 할지를 알고 해결해야함
def solution(line):
    line_list=list(line)
    answer = ''
    q_double=deque()
    d=deque()
    #aabbbc
    #abc
    for i in range(len(line)):
      if i==0:
        d.append(line[i])
      else:
        if line[i]==line[i-1]:
          q_double.append(line[i])
        else:
          if q_double:
            d.append('*')
            q_double.clear()
          d.append(line[i])
    print(d)
    list_answer=list(d)
    answer=''.join(list_answer)
    return answer
  
print(solution('a*bbcc'))