import sys
n,m=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
sum=0
for x in range(0,len(data)-2):
    y=data[x]+data[x+1]+data[x+2]
    if y>sum and y<=m:
        sum=y
        print(x)
print(sum)
