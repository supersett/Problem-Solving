#완전 탐색의 유연한 생각
import sys,itertools
from collections import deque

input=sys.stdin.readline

#k가 5보다 작은경우 어떤 글자도 읽을 수 없다.
N,K=map(int,input().split())
target=[]

# for i in range(N):
#   word=input().rstrip()
#   target.append(word[4:-4])

# print(target)



#word : 각 단어의 비트마스킹 한 정수를 저장해놓는다.
words = [0] * N
ans = 0
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    # word 배열에 각 문자의 비트마스킹 저장
    for x in temp:
        words[i] |= (1 << (ord(x) - ord('a')))

#print(words)

if K<5:
  print(0)
else:
   # candidate : 필수 글자를 제외한 알파벳
    # need : 필수 알파벳
    candidate = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    i_know=['a','n','t','i','c']
    for i in list(itertools.combinations(candidate,K-5)):
      each=0
      res=0
      for j in i_know:
        each |=(1<<(ord(j)-ord('a')))
      for j in i:
        each |=(1<<(ord(j)-ord('a')))
        
      for j in words:
        if each&j==j:
          res+=1
      
      if ans<res:
        ans=res
    print(ans)