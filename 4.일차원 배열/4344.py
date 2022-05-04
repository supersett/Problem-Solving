import sys
n=int(sys.stdin.readline())
data=[]

for x in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

for i in data:
    scoreList=i[1:len(i)]
    