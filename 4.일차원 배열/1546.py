import sys
n=int(sys.stdin.readline())
sum=0
data=list(map(int,sys.stdin.readline().split()))
b=max(data)

for y in range(0,len(data)):
    data[y]=int((data[y]*100)/b)
    
for y in range(0,len(data)):
    sum+=data[y]
average=sum/n

print(average)