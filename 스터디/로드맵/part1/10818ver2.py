import sys

input=sys.stdin.readline

N=int(input())
target=list(map(int,input().split()))

minnum=min(target)
maxnum=max(target)

print(str(minnum)+' '+str(maxnum))


# n = int(input()) #숫자입력
# x = list(map(int,input().split()))
# print(min(x), max(x))