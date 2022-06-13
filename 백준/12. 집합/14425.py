import sys

listq=list(map(int,sys.stdin.readline().split()))
n=listq[0]
m=listq[1]
data=[]
target=[]
count=0

for x in range(n):
    data.append(sys.stdin.readline().rstrip())

for y in range(m):
    target.append(sys.stdin.readline().rstrip())

data_set=set(data)

for k in target:
    if k in data_set:
        count+=1
#print(data)
#print(target_set)
print(count)