from collections import deque

def bfs(arr, n, m, s, t):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque()
    dq.append((s, t, str(arr[s][t]), {(s, t)}))
    max_int = 0
    while dq:
        x, y, num_str, visited = dq.popleft()
        if len(num_str) == 4:
            max_int = max(max_int, int(num_str))
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if (nx, ny) not in visited:
                next_num_str = num_str + str(arr[nx][ny])
                next_visited = visited | {(nx, ny)}
                dq.append((nx, ny, next_num_str, next_visited))
    return max_int

def solution(Board):
    # 인접한 4개를 선택했을 때, 찾을 수 있는 가장 큰 정수 반환
    n, m = len(Board), len(Board[0])
    max_value = 0
    for i in range(n):
        for j in range(m):
            max_value = max(max_value, bfs(Board, n, m, i, j))
    return max_value