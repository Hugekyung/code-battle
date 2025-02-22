# 나이트의 이동 7562번
# 최소 몇번 -> bfs

from collections import deque

def bfs(i, j, gx, gy, m):
    move = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
    visited = [[0] * m for _ in range(m)]
    dq = deque()
    dq.append(((i, j), 0))
    while dq:
        (x, y), cnt = dq.popleft()
        for mx, my in move:
            nx = x + mx
            ny = y + my
            if nx < 0 or ny < 0 or nx >= m or ny >= m or visited[nx][ny]:
                continue
            if not visited[nx][ny]:
                if nx == gx and ny == gy:
                    return cnt + 1
                visited[nx][ny] = 1
                dq.append(((nx, ny), cnt+1))

n = int(input())
result = []
for _ in range(n):
    m = int(input())
    x, y = map(int, input().split())
    gx, gy = map(int, input().split())
    if x == gx and y == gy:
        result.append(0)
        continue
    result.append(bfs(x, y, gx, gy, m))

for r in result:
    print(r)