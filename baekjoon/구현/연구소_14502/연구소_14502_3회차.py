# 14052번 연구소 - 골드4
# 전체를 돌면서 벽 3개 세우기
# 벽 3개를 세운 케이스별로 바이러스가 퍼졌을 때, 안전지대(0)의 개수가 가장 많은 경우를 찾기
# 브루트포스(벽 세우기) + bfs(바이러스 퍼뜨리기)
# 0: 빈칸, 1: 벽, 2: 바이러스

from collections import deque
import copy, sys

n, m = map(int, sys.stdin.readline().split())
labs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_cnt = 0

def bfs():
    global max_cnt
    labs_copy = copy.deepcopy(labs)
    dq = deque()

    # 바이러스 위치 담기
    for i in range(n):
        for j in range(m):
            if labs_copy[i][j] == 2:
                dq.append((i, j))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif labs_copy[nx][ny] == 0:
                labs_copy[nx][ny] = 2
                dq.append((nx, ny))
    this_cnt = 0
    for rows in labs_copy:
        this_cnt += rows.count(0)
    max_cnt = max(max_cnt, this_cnt)
    return

def make_wall(cnt):
    if cnt == 3:
        bfs() # 바이러스 퍼뜨리기
        return
    for i in range(n):
        for j in range(m):
            if labs[i][j] == 0:
                labs[i][j] = 1 # 벽 세우기
                make_wall(cnt + 1)
                labs[i][j] = 0 # 벽 제거
    return

make_wall(0)
print(max_cnt)