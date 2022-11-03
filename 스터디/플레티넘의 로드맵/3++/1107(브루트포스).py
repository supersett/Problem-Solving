import sys
input=sys.stdin.readline

n=input().rstrip()
list_n=list(n)
m=int(input())
broken_button_list=list(map(int,input().split()))
button_list=[i for i in range(0,10)]

print(button_list)
for i in broken_button_list:
  button_list.remove(i)
print(button_list)
#print(broken_button_list)

#현재위치 100
#현재위치가 100이라면 0을 출력하고 out
#무지성으로 빼는거랑 번호입력하는거랑 비교해서 작은 값 출력
#1.갖고있는 수 중 n과 가장 가까운 수를 만들고(자리값으로 비교)
#2.나머지는 +,- 횟수를 세어주면될듯
target=[]

for i in list_n:
  tmp=10
  #5
  int(i)
  target_num=99
  for j in button_list:
    if abs(int(i)-j)<=tmp:
      target_num=j
      tmp=int(i)-j
  target.append(str(target_num))
#print(target)
target_int=int(''.join(target))
print(target_int)


total_push_cnt=len(n)+abs((int(n)-target_int))

if int(n)=='100':
  print(0)
else:
  print(min(total_push_cnt,abs(int(n)-100)))




