h, w = map(int, input().split())
target = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(target[:i])
    right_max = max(target[i+1:])

    compare = min(left_max, right_max)

    if target[i] < compare:
        ans += compare - target[i]

print(ans)