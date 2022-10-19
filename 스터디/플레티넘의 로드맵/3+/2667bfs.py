from collections import deque


def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    queue = deque()

    queue.append((x, y))
    maps[x][y] = '0'
    done.append((x, y))

    while queue:
        now = queue.popleft()
        cnt += 1

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if(0 <= nx < N) and (0 <= ny < N):
                if maps[nx][ny] == '1' and ((nx, ny) not in done):
                    maps[nx][ny] = '0'
                    queue.append((nx, ny))
                    done.append((nx, ny))
    return cnt


N = int(input())
maps = [list(input()) for _ in range(N)]
done = []
total = 0
result = []


for i in range(N):
    for j in range(N):
        if maps[i][j] == '1':
            result.append(bfs(i, j))
            total += 1

result.sort()
print(total)
for i in range(total):
    print(result[i])