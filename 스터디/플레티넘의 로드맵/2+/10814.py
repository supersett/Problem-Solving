import sys

n=int(sys.stdin.readline().rstrip())
answer=[]

for _ in range(n):
    x,y=sys.stdin.readline().split()
    answer.append([int(x),y])

answer.sort(key=lambda x:(x[0]))

for i in answer:
    print(str(i[0])+" "+i[1])