from collections import Counter
import sys

n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
data_target=list(map(int,sys.stdin.readline().split()))
#해당 원소들이 몇 번 등장했는지 세어 딕셔너리 형태로 반환
count =Counter(data)
for i in range(len(data_target)):
    if data_target[i] in count:
        print(count[data_target[i]],end=" ")
    else:
        print(0,end=" ")
