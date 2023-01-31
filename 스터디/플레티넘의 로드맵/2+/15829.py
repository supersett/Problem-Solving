import sys
from collections import defaultdict
input=sys.stdin.readline

n=int(input())

target=list(input().rstrip())
#print(target)

## 알파벳과 숫자를 dic 형식으로 대응해줌
eng='abcdefghijklmnopqrstuvwxyz'
list_eng=list(eng)
numb=[]
for i in range(1,27):
  numb.append(i)

dic={}
for i in range(len(numb)):
  dic[list_eng[i]]=numb[i]

#print(dic)

ans=0
for i in range(n):
  ans+=(dic[target[i]]*(31**i))%1234567891

print(ans%1234567891)