from itertools import combinations

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True
  
#nums = [1,2,3,4]
#combi = list(combinations(nums, 2))

def solution(nums):
    answer = 0
    combi=list(combinations(nums,3))
    for i in combi:
      sum_num=sum(i)
      if is_prime_number(sum_num):
        answer+=1
    return answer
