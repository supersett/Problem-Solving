import sys
from collections import defaultdict
#x,y=map(int,sys.stdin.readline().split())
#dic={}
#print(x,y)

#x의 약수를 구할때 나누기 연산자를 이용할건데
#단순히 전부 도는게 아니라
#i로 나눴을때, 나누기연산이 성립을 한다 = i뿐만아니라 몫도 약수임 을 알 수 있음
#일단 N 이면 N/2 까지만 확인하면 됨

#근데 N번째 약수를 바로 찾고싶단 말이지. dic로 늘어날때마다 자동 추가값을 주고싶음
#정렬이 필요하겠네 하
#1 2 4 8 16

# ans=[1,x]
# for i in range(2,(x//2)):
#   if x%i==0:
#     ans.append(i)
#     if i**2!=x:
#       ans.append(x//i)
# print(ans)
# sett=set(ans)
# setted_list=list(sett)
# ans_sorted=sorted(setted_list)
# print(ans_sorted)
# num=len(ans_sorted)

# if num<y:
#   print(0)
# else:
#   print(ans_sorted[y-1])

N, K = map(int, input().split())
cnt = 0
for i in range(1, N+1):
    if N%i == 0:
        cnt += 1
        if cnt == K:
            print(i)
            break
if cnt < K:
    print(0)

# 와 이거지.. 