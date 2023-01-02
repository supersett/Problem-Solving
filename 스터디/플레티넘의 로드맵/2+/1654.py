import sys

input=sys.stdin.readline

K,N=map(int,input().split())
what_i_got=[]

for _ in range(K):
  what_i_got.append(int(input()))

print(what_i_got)

## 경계조건 10만 .. NlogN 이면 풀 수 있다.
ss=sum(what_i_got)

per=ss/N

print(per)

#이분탐색, 매개변수 탐색
#이분탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘

#재귀함수로 구현하는 이분탐색
def binary_search(array,target,start,end):
  if start > end:
    return None
  mid =(start+end)//2
  
  if array[mid]==target:
    return mid
  elif array[mid]>target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)
  
#반복문으로 구현한 이분탐색
def binary_search2(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    
    #원하는 값 찾은 경우 인덱스 반환
    if array[mid]==target:
      return mid
    
    #원하는 값이 중간점의 값보다 작은 경우 왼쪽부분(절반의 왼쪽) 확인
    elif array[mid]>target:
      end=mid-1
    else:
      start=mid+1
  
  return None
  
  
  
  