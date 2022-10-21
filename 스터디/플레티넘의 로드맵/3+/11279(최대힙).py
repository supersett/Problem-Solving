import heapq
import sys

heap=[]
ans=[]
n=int(sys.stdin.readline().rstrip())

for _ in range(n):
    n=int(sys.stdin.readline().rstrip())
    if n==0:
        if not heap:
            ans.append(0)
            continue
        ans.append(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-n,n))

for i in ans:
    print(i)
