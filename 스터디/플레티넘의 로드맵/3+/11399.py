import sys

n=int(sys.stdin.readline().rstrip())

target=list(map(int,sys.stdin.readline().split()))

target.sort()
ans=0
total=[]
#print(target)
# 1 2 3 3 4
for i in target:
    ans+=i
    total.append(ans)
    
print(sum(total))