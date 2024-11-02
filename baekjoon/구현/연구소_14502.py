# 연구소 14502번
# 1. 벽 3개를 세우는 경우 탐색 -> 브루트포스
# 2. 2(바이러스)가 퍼질 수 있는 곳까지 퍼트린다 -> bfs
# 3. 모든 바이러스가 퍼진 labs에서 0의 개수를 센다
# 4. 모든 과정을 반복하며 max 값을 구한다
from collections import deque
import copy, sys

n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]
max_cnt = 0

# bfs로 2가 있는 곳을 시작점으로 해서 2를 퍼트리기
def bfs():
    global max_cnt
    cnt = 0
    lab_c = copy.deepcopy(lab)
    dq = deque()

    # 2의 위치 추가
    for i in range(n):
        for j in range(m):
            if lab_c[i][j] == 2:
                dq.append((i, j))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = mx[i] + x
            ny = my[i] + y
        
            if (n > nx >= 0) and (m > ny >= 0):
                if lab_c[nx][ny] == 0:
                    lab_c[nx][ny] = 2
                    dq.append((nx, ny))

    # 0의 개수 세기
    for row in lab_c:
        cnt += row.count(0)

    max_cnt = max(max_cnt, cnt)

# 연구소에 벽 3개 세우기 - 재귀버전
def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1 # 벽 세우기
                make_wall(cnt + 1) # 다음 벽을 세우기 위해 재귀
                lab[i][j] = 0 # 다음 반복문을 위해 벽 제거

make_wall(0)
print(max_cnt)