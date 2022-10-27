def solution(skill, skill_trees):
    answer = 0
    for target_skill in skill_trees:
      s=''
      for i in target_skill:
        if i in skill:
          s+=i
      if s == skill[:len(s)]:
        answer+=1
    
    return answer