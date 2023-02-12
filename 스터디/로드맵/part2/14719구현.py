import sys
input=sys.stdin.readline
#https://velog.io/@jxlhe46/%EB%B0%B1%EC%A4%80-14719%EB%B2%88.-%EB%B9%97%EB%AC%BC

a,b=map(int,input().split())
target=list(map(int,input().split()))

#print(target)

#현재 now
#전단계 before
#현재 빗물 water
#전체 빗물 total
now=0
before=0
water=0
total_water=0

#차이로 계산해볼까?
#3 0 1 4
#-3 1 3

#결국에는 내려갔을때 분기점이 시작된다.
#전거와 비교했을때 현재 내려갔을때
#1)다음것이 올라간다
#2)다음것이 똑같은 높이다
#3)다음것이 한칸 더 내려간다

ground=[]

#내려갔다(내려갔을때 높이 저장)가 올라간 상황에 빗물을 더해준다.
#내려가기 시작한 높이 , 올라간 높이 중 더 작은것으로 넣고 계산해야함
#내려갔다가 내려가면 
down_start_h=0
switch=False

for i in range(1,b):
  if target[i]<target[i-1] and switch==False:
    #내려가기 시작할때 높이 저장
    down_start_h=target[i-1]
    switch=True
  #한번 내려갔다는걸 인지한 상황임
  if switch:
    #내려갔을때
    if target[i]<target[i-1]:
      ground.append(target[i])
    #그대로 일때
    elif target[i]==target[i-1]:
      ground.append(target[i])
    #올라갔을 때
    else:
      #첫높이보다 올라가면 빗물 저장하고 변수값들 초기화
      if target[i]>=down_start_h:
        water=((down_start_h*(len(ground)))-sum(ground))
        total_water+=water
        water=0
        switch=False
        ground.clear()
        down_start_h=0
      
      #첫높이보다 덜 올라가면 아직 진행 여지가 있음, 마지막일땐 계산 해야함
      else:
        ground.append(target[i])
        water=((target[i]*(len(ground)))-sum(ground))

#마지막일땐 계산 해야함
if water!=0:
  total_water+=water
  
print(total_water)


      
      
