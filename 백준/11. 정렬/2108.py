import sys
from collections import Counter
import statistics

n=int(sys.stdin.readline())
data=[]
for x in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()

cnt=Counter(data).most_common(2)

print(round(sum(data)/n))
print(statistics.median(data))

if len(data)>1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
        

print(max(data)-min(data))
