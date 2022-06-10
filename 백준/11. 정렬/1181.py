import sys

n=int(sys.stdin.readline())

data=[]
for x in range(n):
    k=(sys.stdin.readline().rstrip())
    data.append(k)

#중복제거된 배열
newData=list(set(data))

newData.sort()
newData.sort(key=lambda x:len(x))

for i in newData:
    print(i)