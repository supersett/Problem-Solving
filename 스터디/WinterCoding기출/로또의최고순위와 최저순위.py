def solution(lottos, win_nums):
    answer = []
    highest=0
    lowest=0
    same_num=0
    num_of_zero=0
    set_win_nums=set(win_nums)
    
    for i in lottos:
      if i ==0:
        num_of_zero+=1
      if i in set_win_nums:
        same_num+=1
        
    if same_num==6:
      lowest=1
    elif same_num==5:
      lowest=2
    elif same_num==4:
      lowest=3
    elif same_num==3:
      lowest=4
    elif same_num==2:
      lowest=5
    
    highest=lowest+num_of_zero
    answer=[lowest,highest]
    return answer
  
  