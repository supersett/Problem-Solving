#enumerate,zip


def solution(enroll, referral, seller, amount):
    money=[0 for _ in range(len(enroll))]
    
    #이름:key, 인덱스:value로 하는 딕셔너리
    dict={}
    for i,e in enumerate(enroll):
      dict[e]=i
    
    for s,a in zip(seller,amount):
      m=a*100
      while s!="-" and m>0:
        idx=dict[s]
        money[idx]+=m-m//10
        
        m//=10
        s=referral[idx]
    return money
  
#이문제는 재귀, 한번에 돌린다. 흐름에 맞춰서. 좋은문제인것같음.