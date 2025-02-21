# 단지 번호 붙이기 dfs
# 재귀방식 구현

def dfs(x, y, arr, visited):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if arr[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny, arr, visited)
    return

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j]and not visited[i][j]:
            cnt = 0
            dfs(i, j, arr, visited)
            result.append(cnt)

print(len(result))
for val in sorted(result):
    print(val)
