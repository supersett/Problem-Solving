


def solution(w,h):
    answer = 1
    min_num=0
    for i in range(min(w,h),0,-1):
      if w%i==0 and h%i==0:
        min_num=i
        break
    total_before=w*h
    
    if min_num==1:
      answer=total_before-(w+h-1)
    elif min_num>1:
      answer=total_before-min_num*((w//min_num)+(h//min_num)-1)
    
    
    return answer
  
#최대공약수 구하기
