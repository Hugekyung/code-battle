# 토마토 7576번

from collections import deque

def bfs(dq, arr, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    max_days = 0
    while dq:
        x, y, days = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1
                add_days = days + 1
                max_days = max(add_days, max_days)
                dq.append((nx, ny, add_days))

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                return -1
    return max_days

def main(n, m, arr):
    days = 0
    dq = deque()
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                dq.append((i, j, 0))

    if not dq:
        return -1
    if len(dq) > 0:
        days = bfs(dq, arr, n, m)
    return days

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
print(main(n, m, arr))