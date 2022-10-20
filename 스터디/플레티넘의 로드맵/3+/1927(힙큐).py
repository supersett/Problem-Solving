import heapq
import sys
heap=[]
ans=[]
#heapq.heappush(heap,)

n=int(input().rstrip())

for _ in range(n):
    k=int(sys.stdin.readline().rstrip())
    if k==0:
        if not heap:
            ans.append("0")
        else:
            ans.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap,k)
    
for i in ans:
    print(i)