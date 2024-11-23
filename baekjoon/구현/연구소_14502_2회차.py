# 연구소 14502번 2회차 풀이
from collections import deque
import copy, sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]
max_cnt = 0

def bfs():
    global max_cnt
    dq = deque()
    lab_copy = copy.deepcopy(arr)

    # 2(바이러스) 큐에 담기
    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] == 2:
                dq.append((i, j))

    # 2를 하나씩 꺼내서 바이러스 퍼트리기
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = mx[i] + x
            ny = my[i] + y
            
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if not lab_copy[nx][ny]:
                lab_copy[nx][ny] = 2
                dq.append((nx, ny))

    safe_cnt = 0
    for row in lab_copy:
        safe_cnt += row.count(0)

    max_cnt = max(max_cnt, safe_cnt)

# 벽 3개 세우기
def make_wall(cnt):
    if cnt == 3:
        bfs() # 바이러스 퍼트리기
        return
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                arr[i][j] = 1
                make_wall(cnt + 1) # 다음 벽 세우기
                arr[i][j] = 0 # 하나의 케이스에 대해 안전지역 개수 세고 나서 다시 원복하기

make_wall(0)
print(max_cnt)