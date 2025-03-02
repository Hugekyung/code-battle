# 벽 부수고 이동하기 2206번
# 최단 경로 - bfs
# 벽을 1개까지 부술 수 있음
# 문제해결의 힌트 ✅
#   1.	visited를 3차원 배열 visited[x][y][wall]로 변경해서 벽을 부순 경우와 부수지 않은 경우를 구별한다.
# 	2.	if not visited[nx][ny]: → if not visited[nx][ny][wall]:로 변경.
# 	3.	벽을 부수고 이동한 경우에는 visited[nx][ny][1] = 1로 설정.
# 	4.	벽을 부수지 않고 이동한 경우에는 visited[nx][ny][wall] = 1로 설정.

from collections import deque

def bfs(arr, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)] # 3차원 배열(x, y, wall)
    dq = deque()
    dq.append((0, 0, 1, 0)) # (x, y, 이동 거리, 벽 부순 여부)
    while dq:
        x, y, cnt, wall = dq.popleft() # wall: 벽을 부쉈는지 여부(boolean)
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 1 and not wall and not visited[nx][ny][1]:
                visited[nx][ny][1] = 1
                dq.append((nx, ny, cnt + 1, 1))
            elif arr[nx][ny] == 0 and not visited[nx][ny][wall]:
                visited[nx][ny][wall] = 1
                dq.append((nx, ny, cnt + 1, wall))
    return -1

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
print(bfs(arr, n, m))