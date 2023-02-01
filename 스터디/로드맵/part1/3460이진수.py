import sys

input=sys.stdin.readline

#n<1000000
#10만 => NlogN 이면 풀수 있다.

#내 문제 = 너무 어렵게 생각한다!!!

T=int(input())
target=[]

for i in range(T):
  target.append(int(input()))

#print(target)

#13 = 1101
#6 1
#정수 n을 이진수로 변환하는 함수
def translate_to_2(n,lists):
  a=n//2
  b=n%2
  lists.append(b)
  if a==0:
    return lists
  else:
    return translate_to_2(a,lists)

ans=[]

for i in target:
  anslist=[]
  num_list=translate_to_2(i,anslist)
  count=0
  for j in range(len(num_list)):
    if num_list[j]==1:
      ans.append(j)

print(*ans)
  

