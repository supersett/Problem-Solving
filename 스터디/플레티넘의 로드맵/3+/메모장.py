n, m, k = map(int, input().split())
s = [[0] * m for i in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = []
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            s[j][k] = 1
print(s)