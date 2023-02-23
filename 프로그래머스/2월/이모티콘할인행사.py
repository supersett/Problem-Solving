import sys

#[우선순위]
#1.서비스 가입자를 최대한 늘린다
#2.이모티콘 판매액을 최대한 늘린다

#n명의 카톡사용자 / m개의 이모티콘을 할인해서 판매
#할인율은 다르고 10,20,30,40 중 하나로 설정

#[사용자들]
#사용자들은 자신의 기준에 따라 일정비율 이상 할인하는 이모티콘을 모두 구매
#이모티콘 구매비용 합이 일정가격 이상이면, 구매 취소하고 서비스 가입
#dfs

emoticons=[1300, 1500, 1600, 4900]
users=[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]

users.sort(key=lambda x:(x[0],x[1]))
discount_table =[0.6, 0.7, 0.8, 0.9, 1]

print(users)
#[[5, 5900], [11, 5200], [23, 10000], [27, 9200], [32, 6900], [40, 2900], [40, 3100]]
num_of_emo=len(emoticons)
discount=[5]*num_of_emo

def solution(users, emoticons):

  answer = [0, 0]
  data = [10 ,20, 30, 40]
  discount = []
    
  # 이모티콘 할인율 구하기
  def dfs(temp, depth):
      if depth == len(temp):
          discount.append(temp[:])
          return
      for d in data:
          temp[depth] += d
          dfs(temp, depth + 1)
          temp[depth] -= d
    
  dfs([0] * len(emoticons), 0)
  print(discount)
  
  answer = []
  return answer

solution([[40, 10000], [25, 10000]],[7000, 9000])