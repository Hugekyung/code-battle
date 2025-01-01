# 14502번 연구소 - 4회차 풀이
# 벽을 3개 세운다
# 바이러스를 시작점으로 해서 바이러스 퍼뜨리기
# 남은 안전영역 개수 세고, max_cnt 갱신하기
from collections import deque
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0
mx, my = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs(): # 바이러스 퍼뜨리기
    global max_cnt

    dq = deque()
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                dq.append((i, j))
    lab_copy = copy.deepcopy(lab)

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if lab_copy[nx][ny] == 0:
                lab_copy[nx][ny] = 2
                dq.append((nx, ny))

    cnt = 0
    for row in lab_copy:
        cnt += row.count(0)
    max_cnt = max(cnt, max_cnt)
    return

def make_wall(cnt): # 벽 3개 세우기
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(cnt + 1)
                lab[i][j] = 0

make_wall(0)
print(max_cnt)