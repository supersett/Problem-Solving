import sys

n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
data_target=list(map(int,sys.stdin.readline().split()))

cnt_data=[]
for y in data_target:
    cnt_data.append(data.count(y))
for x in cnt_data:
    print(x,end=" ")