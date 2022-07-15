import sys

N, P = map(int, input().split())
cnt = 0
lst = [[] for _ in range(7)]

for i in range(N):
    n, p = map(int, sys.stdin.readline().split())
    if not lst[n-1]:
        lst[n-1].append(p)
        cnt += 1
    else:
        while lst[n-1] and p < lst[n-1][-1]:
            lst[n-1].pop()
            cnt += 1
        if not lst[n-1] or p > lst[n-1][-1]:
            lst[n-1].append(p)
            cnt += 1
        else:
            pass
print(cnt)