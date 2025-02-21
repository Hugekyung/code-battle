# 백준 - 단지번호 붙이기 2667번
# dfs -> 모든 시작점으로부터 연결된 집의 개수를 list에 저장

from collections import deque

def bfs(i, j, arr, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque()
    dq.append((i, j))
    cnt = 1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dq.append((nx, ny))
                cnt += 1
    return cnt
                

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            result.append(bfs(i, j, arr, visited))

print(len(result))
for cnt in sorted(result):
    print(cnt)
