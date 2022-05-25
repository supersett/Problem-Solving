import sys

n=int(sys.stdin.readline())
data=[]

for x in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()
for y in data:
    print(y)
